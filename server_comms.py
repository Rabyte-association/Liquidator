# pod-głowny skrypt odpalający wszystkie funkcje do sterowania robotem
from time import sleep
import threading
from Comms import decode_server
from Comms import server



def dataHandler():
    while True:
        try:
            decode_server.datahold.data = server.datahold.data
        except:
            print("err2")


def Initialize(PORT):
    thread_websockets = threading.Thread(target = server.Initialize, args=[PORT])
    thread_decode = threading.Thread(target=decode_server.Initialize)
    thread_handler = threading.Thread(target = dataHandler)

    thread_decode.start()
    thread_websockets.start()
    thread_handler.start()
