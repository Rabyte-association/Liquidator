import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import time
import threading


class Stream():

    host = ''
    port = ''
    frame = None
    alive = True

    def Initialize(self):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect((self.host, self.port))

        data = b''
        payload_size = struct.calcsize("L")

        while True:

            # Retrieve message size
            try:
                while len(data) < payload_size:
                    data += clientsocket.recv(4096)

                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("L", packed_msg_size)[0]

                # Retrieve all data based on message size
                while len(data) < msg_size:
                    data += clientsocket.recv(4096)

                frame_data = data[:msg_size]
                data = data[msg_size:]
            except:
                print('error')
                break

            # Extract frame
            self.frame = pickle.loads(frame_data)

            if not self.alive:
                break

BASE_PORT = 8200

def Initialize(camera_index, server_ip):
    stream = [Stream() for i in range(len(camera_index))]
    thread = []
    for i in range(len(camera_index)):  # creating threads
        stream[i].port = BASE_PORT + i
        stream[i].host = server_ip

        thread.append(threading.Thread(target=stream[i].Initialize))
        thread[i].start()

        print('Camera created')
    while True:
        frame = stream[0].frame
        try:
            for i in range(1, len(stream)):  # frames merger
                frame = np.concatenate((frame, stream[i].frame), axis=1)
        except:
            print('merging error. wait...')
            time.sleep(1)

        try:
            cv2.imshow('Liquidator Video', frame)
        except:
            print('frame error. wait...')
            time.sleep(1)

        key = cv2.waitKey(1)
        if key == ord('q'):  # killing all threads
            for i in range(len(thread)):
                stream[i].alive = False
            break
