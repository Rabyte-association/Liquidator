#glowny skrypt uruchamiajacy wszytskie pozostale po stronie robota
from time import sleep
import threading
from Comms import decode_server
from Comms import server
from video import video_server

'''def dataHandler():
    while True:
        decode.WSrecv = recv.data

recv = server.Receiveclass()
recv.HOST = "localhost"
recv.PORT = 8766
decode = decode_server.Decoder()

thread_websockets = threading.Thread(target = recv.Initialize)
thread_decode = threading.Thread(target=decode.Initialize)
thread_handler = threading.Thread(target = dataHandler)

thread_decode.start()
thread_websockets.start()
thread_handler.start()'''

thread_video = threading.Thread(target=video_server.Initialize, args=[[0], [[1280, 720]]]) #jako argument tablica z indeksami kamer i tablica z rozdzielczosciami
thread_video.start()



