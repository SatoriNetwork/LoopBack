''' a simple websocket server for testing purposes '''
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 5001):
        await asyncio.Future()  # run forever

asyncio.run(main())
