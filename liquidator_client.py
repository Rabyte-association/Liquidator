#glowny skrypt uruchamiajacy wszytskie pozostale po stronie sterowania

import threading

from controller import controller
from controller import emergencybutton
from video import video_client

thread_video = threading.Thread(
    target=video_client.Initialize, args=[[0], 'raspi']) # jako argumenty kolejno indeksy kamer w tablicy i ip serwera



thread_video.start()
