import socket
import pickle
from time import sleep


HOST = 'localhost'    # The remote host
PORT = 8766             # The same port as used by the server
global data
data = '0'

def sender():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print("connected", sock.getsockname())
    while True:
        sock.sendall(data)
        sleep(0.1)