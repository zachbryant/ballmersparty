from typing import Dict, List

from .user import User
from .round import Round
from .action import Action, ActionTypes
from .problem import ProblemManager
from .logging import logger

import random
import itertools
import string
import asyncio

CODE_LENGTH = 4  # Length of the generated game party codes


class GameManager:

    current_games: Dict[str, "GameSession"] = {}  # Active games

    # Create a game party code
    def generate_code(self):
        letters = string.ascii_uppercase
        return "".join(random.choice(letters) for i in range(CODE_LENGTH))

    async def join_or_create_game(self, user: User, join_code):
        if join_code in self.current_games:
            await self.join_game(user, join_code)
        else:
            await self.create_game(user, join_code)

    async def create_game(self, user: User, join_code) -> "GameSession":
        session = GameSession(join_code, user)
        self.current_games[join_code] = session
        await session.emit_state()

    async def join_game(self, user: User, join_code: str):
        if join_code not in self.current_games:
            return False

        session = self.current_games[join_code]
        session.add_user(user)
        await session.emit_state()

    def delete_game(self, join_code: str):
        current_game = self.current_games.pop(join_code)
        current_game.stop_game()

    async def process_game_action(self, user: User, action: Action):
        logger.info(f"Processing action '{action.type_}' from '{user.username}'")
        if user.game_code and user.game_code in self.current_games:
            await self.current_games[user.game_code].process_action(user, action)


class GameStateNodes:
    PREGAME = "pregame"
    CORRAL = "corral"
    ROUND = "round"
    ENDGAME = "endgame"


GAME_STATE_TABLE = {
    GameStateNodes.PREGAME: [GameStateNodes.CORRAL],
    GameStateNodes.CORRAL: [GameStateNodes.ROUND],
    GameStateNodes.ROUND: [GameStateNodes.CORRAL, GameStateNodes.ENDGAME],
    GameStateNodes.ENDGAME: [],
}


class GameState:
    current_state = GameStateNodes.PREGAME

    def _can_advance(self, state):
        if state in GAME_STATE_TABLE[self.current_state]:
            return True
        else:
            return False

    def to_corral(self):
        if self._can_advance(GameStateNodes.CORRAL):
            self.current_state = GameStateNodes.CORRAL
            return True
        else:
            return False

    def to_round(self):
        if self._can_advance(GameStateNodes.ROUND):
            self.current_state = GameStateNodes.ROUND
            return True
        else:
            return False

    def to_endgame(self):
        if self._can_advance(GameStateNodes.ENDGAME):
            self.current_state = GameStateNodes.ENDGAME
            return True
        else:
            return False

    def is_pregame(self):
        return self.current_state == GameStateNodes.PREGAME

    def is_corral(self):
        return self.current_state == GameStateNodes.CORRAL

    def is_round(self):
        return self.current_state == GameStateNodes.ROUND

    def is_endgame(self):
        return self.current_state == GameStateNodes.ENDGAME

    def get(self):
        return self.current_state


NUMBER_OF_ROUNDS = 5


class GameSession:
    join_code: str
    party_master: str
    current_round: Round
    num_rounds_played: 0
    users: List[User]

    def __init__(self, join_code, party_master: User):
        if not isinstance(join_code, str) or not isinstance(party_master, User):
            raise TypeError

        self.join_code = join_code
        self.party_master = party_master
        self.game_state = GameState()
        self.num_rounds_played = 0
        self.current_round = None
        self.problem_manager = ProblemManager()
        self.users = []
        self.add_user(party_master)

        logger.info(f"New GameSession. JoinCode: {join_code}")

    def add_user(self, user: User):
        if not self.game_state.is_pregame():
            return

        for user_ in self.users:
            if user_ == user:
                return

        self.users.append(user)
        user.set_game_code(self.join_code)
        logger.info(f"Added '{user.username}' to '{self.join_code}'")

    async def remove_user(self, user: User):
        if not self.game_state.is_pregame():
            return

        self.users.remove(user)
        await self.emit_state()

    async def remove_user_by_sid(self, sid):
        for user in self.users:
            if user.sid == sid:
                await self.remove_user(user)

    def _get_users_json_list(self):
        users = []
        for user in self.users:
            users.append(
                {
                    "username": user.username,
                    "sid": user.sid,
                    "ready": self.current_round.user_ready[user]
                    if self.current_round
                    else None,
                }
            )

        return users

    async def emit_state(self):
        global_state = {
            "join_code": self.join_code,
            "state": self.game_state.get(),
            "num_rounds_played": self.num_rounds_played,
            "num_total_rounds": NUMBER_OF_ROUNDS,
            "users": self._get_users_json_list(),
            "problem": None,
            "stats": None,
        }

        if self.game_state.is_round():
            global_state["problem"] = self.current_round.get_problem_description()

        if self.game_state.is_corral() or self.game_state.is_endgame():
            global_state["stats"] = {"42": "69"}

        tasks = []
        for user in self.users:
            tasks.append(
                user.emit(
                    "game_state",
                    {
                        "global": global_state,
                        "user": {
                            "tests_passed": 0,
                            "tests_failed": 0,
                            "username": user.username,
                            "sid": user.sid,
                            "ready": self.current_round.user_ready[user]
                            if self.current_round
                            else None,
                            "is_party_master": user == self.party_master,
                        },
                    },
                )
            )

        await asyncio.gather(*tasks)

    async def user_ready(self, user: User):
        if not self.game_state.is_corral():
            return

        self.current_round.set_user_ready(user)
        if self.current_round.is_everyone_ready():
            self.game_state.to_round()

        await self.emit_state()

    async def process_submission(self, user: User, submission_data):
        if not self.game_state.is_round():
            return

        logger.info(f"Recieved code from '{user.username}': {submission_data}")
        await self.current_round.submission(user, submission_data)

    async def start_game(self):
        if not self.game_state.is_pregame():
            return

        if len(self.users) == 1:
            return

        logger.info(f"Starting game '{self.join_code}'")
        self.current_round = Round(
            self.users, self.problem_manager.pick_random_problem(), self
        )
        self.game_state.to_corral()
        await self.emit_state()

    def stop_game(self, join_code):
        for user in self.users:
            user.remove_game()

    async def process_action(self, user: User, action: Action):
        logger.info(
            f"Processing action '{action.type_}' from '{user.username}' for game '{self.join_code}'"
        )
        if action.type_ == ActionTypes.DISCONNECTED:
            pass
        elif action.type_ == ActionTypes.READY:
            await self.user_ready(user)

        elif action.type_ == ActionTypes.SUBMIT_ANSWER:
            await self.process_submission(user, action.data)

        elif action.type_ == ActionTypes.KICK_PLAYER:
            if user != self.party_master:
                return False
            await self.remove_user_by_sid(action.data)

        elif action.type_ == ActionTypes.START_GAME:
            if user != self.party_master:
                return False
            await self.start_game()

        return True
