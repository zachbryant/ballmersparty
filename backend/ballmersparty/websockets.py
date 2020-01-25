from socketio import AsyncNamespace
from typing import Dict, Optional
from .user import User


class GameNamespace(AsyncNamespace):
    _user_table: Dict[str, User] = {}

    def __init__(self, namespace, game_manager):
        super().__init__(namespace)
        self.game_manager = game_manager

    def on_connect(self, sid, environ):
        pass

    def on_disconnect(self, sid):
        pass # destroy user

    def on_create_game(self, sid, data):
        self.game_manager.create_game()

    async def on_register(self, sid, data):
        username = data.get("username")

        if not username:
            return

        self._user_table[str(sid)] = User(sid, username, self)
        await self.emit("registered", {"success": True}, room=sid)

    async def on_join_game(self, sid, data):
        join_code = data.get("join_code")
        if not join_code:
            return

        self.game_manager.join_game(self._get_user_from_sid(sid), join_code)

    async def on_game_action(self, sid, data):
        await self.game_manager.process_game_action(self._get_user_from_sid(sid), data)

    def _get_user_from_sid(self, sid) -> Optional[User]:
        return self._user_table.get(str(sid))
