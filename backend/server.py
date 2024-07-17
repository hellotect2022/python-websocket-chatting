import asyncio
import websockets

connected_clients = set()
async def chat_server_init(websocket,path):
    try:
        print(f'websocket ->${websocket}')
        print(f'path ->${path}')
        connected_clients.add(websocket)
        print(f'connected_clients -> ${connected_clients}')

        async for message in websocket:
            print(f'message -> ${message}')
            for client in connected_clients:
                await client.send(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    start_server = await websockets.serve(chat_server_init,"0.0.0.0",7777)
    await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())