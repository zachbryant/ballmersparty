from typing import Dict

from .user import User

import random

class GameManager:

    CODE_LENGTH = 4 # Length of the generated game party codes

    current_games: Dict[str, "GameSession"] = {} # Active games

    # Create a game party code
    def generate_code(self):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letter) for i in range(CODE_LENGTH))

    def create_game(self, user: User, options) -> "GameSession":
        join_code = generate_code()

        # Checks if party code already exists
        while join_code not in self.current_games:
            join_code = generate_code()
        
        session = GameSession(join_code, user)

        current_games.add(join_code, session)

        return join_code

    def join_game(self, user: User, join_code: str):
        if join_code not in self.current_games:
            return False
        self.current_games[join_code].add_user(user)
        return True

    def delete_game(self, join_code: str):
        current_game = current_games.pop(join_code)
        current_game.stop_game()


class GameState:
    pass


class GameSession:
    join_code: str
    party_master: str

    users = []

    def __init__(self, join_code, party_master: User):
        if type(join_code) not str or type(party_master) not User:
            raise TypeError

        self.join_code = join_code
        self.party_master = party_master
        self.game_state = GameState()

    def add_user(self, user: User):
        users.append(user)

    def remove_user(self, user: User):
        users.remove(user)

    def stop_game(self, join_code):
        for user in users:
            user.remove_game()
    


        
