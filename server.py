import asyncio
import websockets
import json

port = 7890
print(f"Server is listening on port {port}")

async def handle_client(websocket, path=None): 
    print(f"Client connected from {path}")
    try:
        async for message in websocket:
            data = json.loads(message)
            response = {
                "reply": f"Hello, {data.get('name', 'Guest')}!",
                "status": "ok"
            }
            await websocket.send(json.dumps(response))  # ✅ Send pure JSON
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handle_client, "127.0.0.1", port):
        await asyncio.Future()  

asyncio.run(main())