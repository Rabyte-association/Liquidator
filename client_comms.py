#pod-główny skrypt odpalający websockety i pada do sterowania klientem

import threading
from time import sleep
import pickle
from Comms import encode_client as encode
from Comms import client


def dataHandler():
    while True:
        client.data = pickle.dumps(encode.Data)         #ta jendna linijka odpowiedzialna jest za dzialanie caleego systemu ;)
        
def Initialize(SERVER_PORT, SERVER_IP):
    thread_encode = threading.Thread(target=encode.Initialize)
    thread_websockets = threading.Thread(target=client.sender, args = (SERVER_PORT, SERVER_IP))
    thread_handler= threading.Thread(target = dataHandler)

    thread_encode.start()
    thread_websockets.start()
    thread_handler.start()
