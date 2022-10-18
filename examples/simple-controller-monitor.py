import time
import threading
import subprocess
import emergencybutton
import controller
import os


def ConsoleInfo():
    prev = pad.button_X
    prev_emer = emer.state
    while True:
        if prev_emer != emer.state or prev != pad.button_X:
            os.system('clear')
            print('button x: ' + str(pad.button_X))
            print('emergency: ' + str(emer.state))
            prev = pad.button_X
            prev_emer = emer.state
            if pad.axisTR.value == 1.0:
                pad.ShowDebug()
        if emer.state == True:
            proc = subprocess.Popen(
                ["pgrep mpv"], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            out = out.decode('utf-8', 'ignore')
            out = out.strip('\r\n')
            if out == '':
                os.system(
                    "mpv emergencystop.mp4 -volume=100 --no-terminal --fullscreen &")
        else:
            proc = subprocess.Popen(
                ["pgrep mpv"], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            out = out.decode('utf-8', 'ignore')
            out = out.strip('\r\n')
            if out != '':
                bash = ("kill " + str(out))
                os.system(bash)
        time.sleep(0.01)


pad = controller.Pad()
emer = emergencybutton.EmergencyButton()

thread_controller = threading.Thread(target=pad.Initialize)
thread_emergencybutton = threading.Thread(target=emer.Initialize)
thread_debug = threading.Thread(target=ConsoleInfo)

thread_controller.start()
thread_emergencybutton.start()
thread_debug.start()
