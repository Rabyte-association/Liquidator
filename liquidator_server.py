import threading

from controller import controller
from controller import emergencybutton
from video import video_server

thread_video = threading.Thread(target=video_server.Initialize, args=[8102])


thread_video.start()
