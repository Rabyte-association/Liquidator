#glowny skrypt uruchamiajacy wszytskie pozostale po stronie robota

import threading

from controller import controller
from controller import emergencybutton
from video import video_server

thread_video = threading.Thread(target=video_server.Initialize, args=[[0,2]]) #jako argument tablica z indeksami kamer


thread_video.start()
