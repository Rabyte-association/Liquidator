import asyncio
import websockets
import acapture
import cv2

SERVER_IP = "192.168.1.28"
SERVER_PORT = 8764

FRAMERATE = 0.0001  # [ t -> 0 ] = faster
CAMERA_INDEX = [0]


async def connection(websocket):
    print("Client connected")

    # open webcam
    try:
        cap = acapture.open(CAMERA_INDEX[0])
    except:
        print("ERROR: Webcam error")
        cap = acapture.open(CAMERA_INDEX[0])

    # get frame from webcam, encode and send to client
    while True:
        check, frame = cap.read()
        if not websocket.open:
            print("Client disconnected")
            print("Waiting for client...")
            cap.destroy()
            break

        if check:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            check, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            frame = bytearray(frame)
            try:
                await websocket.send(frame)
            except:
                print("Connection ERROR")
                print("Waiting for client...")
                cap.destroy()
                break
        await asyncio.sleep(FRAMERATE)


# start server
async def main():
    async with websockets.serve(connection, SERVER_IP, SERVER_PORT):
        print("Waiting for client...")
        await asyncio.Future()

asyncio.run(main())
