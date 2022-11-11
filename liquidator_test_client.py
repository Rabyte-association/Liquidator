#glowny skrypt uruchamiajacy wszytskie pozostale po stronie sterowania

import threading
from time import sleep
import pickle

from Comms import encode_client as encode
from Comms import client
from video import video_client

def dataHandler():
    while True:
        client.data = pickle.dumps(encode.Data)

#thread_video = threading.Thread(target=video_client.Initialize, args=[[0], '192.168.0.40']) # jako argumenty kolejno indeksy kamer w tablicy i ip serwera
thread_print = threading.Thread(target = dataHandler)
thread_encode = threading.Thread(target=encode.Initialize)
thread_websockets = threading.Thread(target=client.sender)
# thread_video.start()
thread_encode.start()
thread_websockets.start()
thread_print.start()
