#glowny skrypt uruchamiajacy wszytskie pozostale po stronie robota
from time import sleep
import threading
import server_comms
from video import video_server

thread_video = threading.Thread(target=video_server.Initialize, args=[[0], [[1280, 720]]]) #jako argument tablica z indeksami kamer i tablica z rozdzielczosciami
thread_video.start()