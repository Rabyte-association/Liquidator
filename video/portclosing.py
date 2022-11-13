import os
import signal
from subprocess import Popen, PIPE

def KillPort(port):
    try:
        process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        for process in str(stdout.decode("utf-8")).split("\n")[1:]:       
            data = [x for x in process.split(" ") if x != '']
            if (len(data) <= 1):
                continue

            os.kill(int(data[1]), signal.SIGKILL)
    except:
        print('port killing error')