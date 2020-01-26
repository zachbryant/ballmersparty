class User:
    _destructors = []
    game_code: bool

    def __init__(self, sid, username, sio_namespace):
        self.sid = str(sid)
        self.username = username
        self.sio_namespace = sio_namespace
        self.game_code = None

    def set_game_code(self, game_code):
        self.game_code = game_code

    def register_desturctor(self, function):
        self._destructors.append(function)

    def destroy(self):
        for destructor in self._destructors:
            destructor()

    async def emit(self, event_name, data):
        await self.sio_namespace.emit(event_name, data, room=self.sid)

    def remove_game_code(self):
        self.game_code = None
