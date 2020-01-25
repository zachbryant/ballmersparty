from typing import Dict

from .user import User
from .round import Round
from .action import Action, ActionTypes

import random
import itertools
import string

CODE_LENGTH = 4  # Length of the generated game party codes


class GameManager:

    current_games: Dict[str, "GameSession"] = {}  # Active games

    # Create a game party code
    def generate_code(self):
        letters = string.ascii_uppercase
        return "".join(random.choice(letters) for i in range(CODE_LENGTH))

    def create_game(self, user: User, options) -> "GameSession":
        join_code = self.generate_code()

        # Checks if party code already exists
        while join_code not in self.current_games:
            join_code = self.generate_code()

        session = GameSession(join_code, user)

        self.current_games[join_code] = session

        return join_code

    def join_game(self, user: User, join_code: str):
        if join_code not in self.current_games:
            return False

        self.current_games[join_code].add_user(user)
        return True

    def delete_game(self, join_code: str):
        current_game = self.current_games.pop(join_code)
        current_game.stop_game()

    def process_game_action(self, user: User, action: Action):
        if user.game_code and user.game_code in self.current_games:
            self.current_games[user.game_code].process_action(user, action)


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


NUMBER_OF_ROUNDS = 5


class GameSession:
    join_code: str
    party_master: str
    current_round: Round
    num_rounds_played: 0
    users = []

    def __init__(self, join_code, party_master: User):
        if isinstance(join_code, str) or isinstance(party_master, User):
            raise TypeError

        self.join_code = join_code
        self.party_master = party_master
        self.game_state = GameState()
        self.num_rounds_played = 0
        self.current_round = None

    def add_user(self, user: User):
        if not self.game_state.is_pregame():
            return

        self.users.append(user)

    def remove_user(self, user: User):
        if not self.game_state.is_pregame():
            return

        self.users.remove(user)

    def remove_user_by_sid(self, sid):
        for user in self.users:
            if user.sid == sid:
                self.remove_user(user)

    def user_ready(self, user: User):
        if not self.game_state.is_corral():
            return

        pass  # TODO:

    def process_submission(self, user: User, submission_data):
        if not self.game_state.is_round():
            return

        pass  # TODO:

    def start_game(self):
        if not self.game_state.is_pregame():
            return

        pass # TODO:

    def stop_game(self, join_code):
        for user in self.users:
            user.remove_game()

    def process_action(self, user: User, action: Action):
        if action.type_ == ActionTypes.DISCONNECTED:
            pass
        elif action.type_ == ActionTypes.READY:
            self.user_ready(user)
        elif action.type_ == ActionTypes.SUBMIT_ANSWER:
            self.process_submission(user, action.data)
        elif action.type_ == ActionTypes.KICK_PLAYER:
            if user != self.party_master:
                return False
            self.remove_user_by_sid(action.data)
        elif action.type_ == ActionTypes.START_GAME:
            if user != self.party_master:
                return False
            self.start_game()

        return True
