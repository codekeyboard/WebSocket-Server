# json_client.py
import asyncio
import websockets
import json

async def chat():
    uri = "ws://127.0.0.1:7890"
    async with websockets.connect(uri) as websocket:
        message = {
            "name": "Abdullah",
            "message": "Hello Server!"
        }
        await websocket.send(json.dumps(message))

        response = await websocket.recv()
        data = json.loads(response)
        print(f"Server replied with JSON: {data}")

asyncio.run(chat())
