import asyncio
import string
import websockets
import signal
from xbox360controller import Xbox360Controller
websockets.connect("ws://192.168.0.69:8765")
global message
global mess
mess = "0"
message = [0,0,0,0,0,0]

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += str(ele)
    mess = str1
    return mess
    
async def hello(mess):
    async with websockets.connect("ws://192.168.0.69:8765") as websocket:
        while True:
            await control()
            await websocket.send(mess)
            await websocket.recv()
            asyncio.Future()

async def control():
        with Xbox360Controller(0, axis_threshold=0.2) as controller:
            # Button A events
            message[0] = 1 #enable
            message[1] = int(controller.axis_l._value_y*5)
            #print("lol")
            mess = listToString(message)

asyncio.run(hello(mess))
