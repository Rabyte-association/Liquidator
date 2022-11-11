import time
import threading
import subprocess
from serial import Serial
import controller
import os
MAX_VEL = -400
MAX_TURN = 100
def ConsoleInfo():
    serial = Serial(
        port='/dev/ttyACM7', baudrate=115200, timeout=.1)
    while True:
        x = pad.leftAxis.y * MAX_VEL
        y = pad.leftAxis.x * MAX_TURN
        serial.write(bytes(str('a' + str(x)), 'utf-8'))
        serial.write(bytes(str('b' + str(y)), 'utf-8'))
       # print(f"x:{x}, y:{y}")
        #pad.ShowDebug()
        if pad.button_X == True:
            while True:
                serial.write(bytes(str('a' + str(0))))
                serial.write(bytes(str('b' + str(0))))
        


pad = controller.Pad()

thread_controller = threading.Thread(target=pad.Initialize)
thread_debug = threading.Thread(target=ConsoleInfo)

thread_controller.start()
thread_debug.start() 