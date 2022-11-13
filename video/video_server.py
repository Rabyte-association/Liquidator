import pickle
import socket
import struct

import cv2
import threading
import sys

sys.path.insert(0, './video')
from portclosing import KillPort

class Stream():

    host = ''
    port = ''
    resolution = [640, 480]
    camera = 0

    def Initialize(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created: ' + str(self.port))

        while True:
            try:
                s.bind((self.host, self.port))
                break
            except:
                KillPort(self.port)

        print('Socket bind complete: ' + str(self.port))
        while True:
            s.listen(10)
            print('Socket now listening: ' + str(self.port))

            clientsocket, addr = s.accept()
            print('client connected at: ' + str(addr))

            cap = cv2.VideoCapture(self.camera) #set camera res
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])

            while True:
                ret, frame = cap.read()
                if not ret:
                    cap.release()
                    cap = cv2.VideoCapture(self.camera)
                    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
                    cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
                    continue

                # Serialize frame
                data = pickle.dumps(frame)

                # Send message length first
                message_size = struct.pack("L", len(data))

                # Then data
                try:
                    clientsocket.sendall(message_size + data)
                except:
                    print('connection error: ' + str(self.port))
                    cap.release()
                    break

BASE_PORT = 8200

def Initialize(camera_index, camera_resolution):
    stream = [Stream() for i in range(len(camera_index))]
    thread = []
    for i in range(len(camera_index)):
        stream[i].port = BASE_PORT + i
        stream[i].camera = camera_index[i]
        stream[i].resolution = camera_resolution[i]
    for i in range(len(camera_index)):
        thread.append(threading.Thread(target=stream[i].Initialize))

    for i in range(len(camera_index)):
        thread[i].start()

