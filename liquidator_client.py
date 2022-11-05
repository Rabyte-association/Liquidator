import threading

from controller import controller
from controller import emergencybutton
from video import video_client

thread_video = threading.Thread(
    target=video_client.Initialize, args=['', 8102])


thread_video.start()
