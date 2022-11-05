import pickle
import socket
import struct

import cv2
import threading


class Stream():

    host = ''
    port = ''
    camera = 0

    def Initialize(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created: ' + str(self.port))

        s.bind((self.host, self.port))
        print('Socket bind complete: ' + str(self.port))
        while True:
            s.listen(10)
            print('Socket now listening: ' + str(self.port))

            clientsocket, addr = s.accept()
            print('client connected at: ' + str(addr))
            cap = cv2.VideoCapture(self.camera)
            while True:
                ret, frame = cap.read()
                if not ret:
                    cap.release()
                    cap = cv2.VideoCapture(self.camera)
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

def Initialize(camera_index):
    stream = [Stream() for i in range(len(camera_index))]
    thread = []
    for i in range(len(camera_index)):
        stream[i].port = BASE_PORT + i
        stream[i].camera = camera_index[i]
    for i in range(len(camera_index)):
        thread.append(threading.Thread(target=stream[i].Initialize))

    for i in range(len(camera_index)):
        thread[i].start()

