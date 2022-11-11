#główny skrypt odpalający websockety i pada do sterowania klientem

import threading
from time import sleep
import pickle

from Comms import encode_client as encode
from Comms import client


def dataHandler():
    while True:
        client.data = pickle.dumps(encode.Data)
        #print(pickle.dumps(encode.Data))
        #print(f"homing:{encode.Data.homing}, hvbarm:{encode.Data.HVB_ARM}, speed:{encode.Data.hvbSpeed}, dir: {encode.Data.hvbDir}, Y; {encode.Data.motorY}, X1: {encode.Data.motorX1}")
        #print(f"Axis TR:{encode.pad.axisTR}, Axis TL: {encode.pad.axisTL}, THumb R X:{encode.pad.rightAxis.x}, Thumb R Y: {encode.pad.rightAxis.y}, Thumb L X: {encode.pad.leftAxis.x} Thumb L Y: {encode.pad.leftAxis.y}")
        #print()
        #sleep(0.5)

thread_encode = threading.Thread(target=encode.Initialize, args = "w")
thread_websockets = threading.Thread(target=client.sender)

thread_encode.start()
thread_websockets.start()

thread_print = threading.Thread(target = dataHandler)
thread_print.start()
