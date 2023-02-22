#glowny skrypt uruchamiajacy wszytskie pozostale po stronie sterowania

import threading
import cumming
import client_comms
from video import video_client

SERVER_IP  = '192.168.1.69'
SERVER_PORT = 8765

#thread_video = threading.Thread(target=cumming.cumming)
#thread_video = threading.Thread(target=video_client.Initialize, args=[1, SERVER_IP]) # jako argumenty kolejno ilość kamer i ip serwera
thread_comms = threading.Thread(target=client_comms.Initialize, args = (SERVER_PORT, SERVER_IP))

#thread_video.start()
thread_comms.start() 

 