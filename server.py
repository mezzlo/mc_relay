import asyncio
import websockets
import os

clients = set()

async def handler(websocket):
    print("Client connected")
    clients.add(websocket)

    try:
        async for message in websocket:
            print("Received:", message)

            for client in clients:
                if client != websocket:
                    await client.send(message)

    finally:
        clients.remove(websocket)

async def main():
    port = int(os.environ.get("PORT", 8080))

    print("Starting WebSocket server on port", port)

    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future()

asyncio.run(main())
