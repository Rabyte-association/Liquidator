import asyncio
import websockets
import cv2
import numpy as np

SERVER_IP = "ws://192.168.0.69:8764"


async def connection():
    async with websockets.connect(SERVER_IP) as websocket:
        while True:
            received = await websocket.recv()
            frame = np.frombuffer(received, np.uint8)
            image = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            cv2.imshow('image', image)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

asyncio.get_event_loop().run_until_complete(connection())
