from typing import Dict

from .user import User


class GameManager:

    current_games: Dict[str, "GameSession"] = {}

    def create_game(self, user: User, options) -> "GameSession":
        raise NotImplementedError

    def join_game(self, user: User, code):
        if code not in self.current_games:
            return False

        self.current_games[code].add_user(user)


class GameState:
    pass


class GameSession:
    join_code: str
    options: object

    def __init__(self, options):
        self.options = options
        self.game_state = GameState()

    def add_user(self, user: User):
        raise NotImplementedError
