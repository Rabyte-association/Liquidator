import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import time


def Initialize(host, port):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))

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
        frame = pickle.loads(frame_data)

        # Display
        try:
            cv2.imshow('frame', frame)
        except:
            print('frame error')

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
