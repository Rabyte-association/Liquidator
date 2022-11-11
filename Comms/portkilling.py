from psutil import process_iter
from signal import SIGKILL
#still in the works
def p(nr):
    for proc in process_iter():
        for conns in proc.get_connections(kind='inet'):
            if conns.laddr[1] == nr:
                proc.send_signal(SIGKILL) 
                continue


port=int(input("Podaj port: "))
p(port)
