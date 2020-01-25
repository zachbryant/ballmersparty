
class User:
    _destructors = []

    def __init__(self, sid, username):
        self.sid = sid
        self.username = username
        self.game_code = None

    def set_game_code(self, game_code):
        self.game_code = game_code

    def register_desturctor(self, function):
        self._destructors.append(function)

    def destroy(self):
        for destructor in self._destructors:
            destructor()

    def remove_game(self):
        pass
