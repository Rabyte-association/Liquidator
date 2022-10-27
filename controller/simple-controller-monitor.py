import time
import threading
import subprocess
import emergencybutton
import controller
import os


def ConsoleInfo():
    prev = pad.button_X
   # prev_emer = emer.state
    
    while True:
        if prev != pad.button_X:
           # os.system('clear')
            print('button x: ' + str(pad.button_X))
           # print('emergency: ' + str(emer.state))
            prev = pad.button_X
           # prev_emer = emer.state
            pad.ShowDebug()

        time.sleep(0.1)


pad = controller.Pad()
emer = emergencybutton.EmergencyButton()

thread_controller = threading.Thread(target=pad.Initialize(0))
thread_emergencybutton = threading.Thread(target=emer.Initialize)
thread_debug = threading.Thread(target=ConsoleInfo)

thread_controller.start()
#thread_emergencybutton.start()
thread_debug.start()
