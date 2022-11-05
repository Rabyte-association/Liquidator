import pickle
import socket
import struct
import sys

import cv2
import numpy as np

HOST = ''


def Initialize(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    s.bind((HOST, port))
    print('Socket bind complete')
    while True:
        s.listen(10)
        print('Socket now listening')

        clientsocket, addr = s.accept()
        print('client connected at: ' + str(addr))
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.release()
                cap = cv2.VideoCapture(0)
                continue

            # Serialize frame
            data = pickle.dumps(frame)

            # Send message length first
            message_size = struct.pack("L", len(data))

            # Then data
            try:
                clientsocket.sendall(message_size + data)
            except:
                print('connection error')
                cap.release()
                break
