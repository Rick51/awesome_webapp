import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')


app = web.Application()
app.router.add_route('GET', '/', index)
web.run_app(app,host='127.0.0.1', port=9000)