import socket
from time import sleep

       # The same port as used by the server
global data
data = '0'

def sender(SERVER_PORT, SERVER_IP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    print(f"Connecting to: {SERVER_IP}, {SERVER_PORT}")

    sock.connect((str(SERVER_IP), int(SERVER_PORT)))

    print("connected", sock.getsockname())

    while True:
        sock.sendall(data)
        sleep(0.01)