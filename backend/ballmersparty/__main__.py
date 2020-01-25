import os

from .config import SERVE_DIST
from .websockets import GameNamespace
from .game import GameManager

import socketio
from aiohttp import web


sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins="*")
app = web.Application()

if SERVE_DIST:
    STATIC_FILES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist")

    async def index(request):
        return web.FileResponse(os.path.join(STATIC_FILES_DIR, "index.html"))

    app.router.add_route("GET", "/", index)
    sio.attach(app)
    app.router.add_static("/", path=STATIC_FILES_DIR, name="static")

else:
    sio.attach(app)

game_manager = GameManager()
sio.register_namespace(GameNamespace("/", game_manager))
web.run_app(app)
