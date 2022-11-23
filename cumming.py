import os
import time
import re

def cumming():
    delta = 0
    while True:
        pid = []
        pid_out_temp = os.popen("pgrep mpv").read()
        pid_out = str(pid_out_temp)
        buff = []
        for c in pid_out:
            if c == '\n':
                pid.append(''.join(buff))
                buff = []
            else:
                buff.append(c)
        else:
            if buff:
                pid.append(''.join(buff))
        if len(pid) == 0 or len(pid) == 1:
            os.system("mpv rtsp://192.168.1.69:8554/cum --force-seekable=yes --profile=low-latency --no-border --no-terminal --geometry=50%x100%+100%+0% &")
            os.system("mpv rtsp://192.168.1.69:8554/cam --force-seekable=yes --profile=low-latency --no-border --no-terminal --geometry=50%x100%+0+0 &")
        if delta == 10:
            os.system("mpv rtsp://192.168.1.69:8554/cum --force-seekable=yes --profile=low-latency --no-border --no-terminal --geometry=50%x100%+100%+0% &")
            os.system("mpv rtsp://192.168.1.69:8554/cam --force-seekable=yes --profile=low-latency --no-border --no-terminal --geometry=50%x100%+0+0 &")
            time.sleep(1)
            for i in pid:
                command = "kill " + str(i)
                os.system(command)
                print('trying to cum in ' + str(i))
            delta = 0
        delta += 1
        time.sleep(1)