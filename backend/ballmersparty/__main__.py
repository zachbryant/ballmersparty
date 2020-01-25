import os

import socketio
from aiohttp import web

STATIC_FILES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist")

sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins="*")
app = web.Application()


async def index(request):
    return web.FileResponse(os.path.join(STATIC_FILES_DIR, "index.html"))


app.router.add_route("GET", "/", index)
sio.attach(app)
app.router.add_static("/", path=STATIC_FILES_DIR, name="static")
