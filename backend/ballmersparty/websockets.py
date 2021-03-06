from socketio import AsyncNamespace
from typing import Dict, Optional
from .user import User
from .logging import logger
from .action import Action
import asyncio


class GameNamespace(AsyncNamespace):
    _user_table: Dict[str, User] = {}

    def __init__(self, namespace, game_manager):
        super().__init__(namespace)
        self.game_manager = game_manager

    def on_connect(self, sid, environ):
        logger.info(f"New client connected. SID: {sid}")

    async def on_disconnect(self, sid):
        logger.info(f"Client disconnected. SID: {sid}")

        user = self._get_user_from_sid(sid)
        if not user:
            return

        await self.game_manager.process_game_action(
            user, Action.get_disconnect_action()
        )

    # def on_create_game(self, sid, data):
    #     user = self._get_user_from_sid(sid)
    #     if not user:
    #         return

    #     self.game_manager.create_game(user, data)

    async def on_register(self, sid, data):
        if self._get_user_from_sid(sid):
            return

        username = data.get("username").strip()

        if not username:
            await self.emit(
                "registered", {"success": False, "error": "Invalid username"}, room=sid
            )
            return

        join_code = data.get("join_code").strip()
        if not join_code:
            await self.emit(
                "registered", {"success": False, "error": "Invalid joincode"}, room=sid
            )
            return

        user = User(sid, username, self)
        self._user_table[str(sid)] = user
        logger.info(
            f"New user registered. USERNAME: {username}, SID: {sid}, JoinCode: {join_code}"
        )

        await self.emit("registered", {"success": True}, room=sid)
        await self.game_manager.join_or_create_game(user, join_code)

    # async def on_join_game(self, sid, data):
    #     join_code = data.get("join_code")
    #     if not join_code:
    #         return

    #     user = self._get_user_from_sid(sid)
    #     if not user:
    #         return

    #     await self.game_manager.join_game(user, join_code)

    async def on_game_action(self, sid, data):
        user = self._get_user_from_sid(sid)
        if not user:
            return

        action = Action.from_dict(data)

        if not action:
            return

        await self.game_manager.process_game_action(user, action)

    def _get_user_from_sid(self, sid) -> Optional[User]:
        return self._user_table.get(str(sid))
