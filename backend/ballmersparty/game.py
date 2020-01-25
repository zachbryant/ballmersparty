from typing import Dict

from .user import User
from .round import Round

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


class GameState:
    pass


class GameSession:

    NUMBER_OF_ROUNDS = 5

    join_code: str
    party_master: str

    users = []

    def __init__(self, join_code, party_master: User):
        if isinstance(join_code, str) or isinstance(party_master, User):
            raise TypeError

        self.join_code = join_code
        self.party_master = party_master
        self.game_state = GameState()
        self.rounds = list(itertools.repeat(Round(users), NUMBER_OF_ROUNDS))

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user: User):
        self.users.remove(user)

    def stop_game(self, join_code):
        for user in self.users:
            user.remove_game()

