import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri=uri) as websocket:
        await websocket.send("hello world!")
        await websocket.recv()


asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
