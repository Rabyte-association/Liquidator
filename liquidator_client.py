#glowny skrypt uruchamiajacy wszytskie pozostale po stronie sterowania

import threading
import client_comms
from video import video_client

<<<<<<< HEAD
SERVER_IP  = '192.168.0.15'
SERVER_PORT = 8767


thread_video = threading.Thread(target=video_client.Initialize, args=[1, SERVER_IP]) # jako argumenty kolejno ilość kamer i ip serwera
thread_comms = threading.Thread(target=client_comms.Initialize, args = (SERVER_PORT, SERVER_IP))

=======
thread_video = threading.Thread(
    target=video_client.Initialize, args=[1, '']) # jako argumenty kolejno ilość kamer i ip serwera
>>>>>>> 65e0fa96e0ced8a0f8ae982468289b5ff77d1e45

#thread_video.start()
thread_comms.start() 
