#glowny skrypt uruchamiajacy wszytskie pozostale po stronie sterowania

import threading

from controller import controller
from controller import emergencybutton
from video import video_client

thread_video = threading.Thread(
    target=video_client.Initialize, args=[1, '']) # jako argumenty kolejno ilość kamer i ip serwera

thread_video.start()
