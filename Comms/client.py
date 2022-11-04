import socket
import encode
import time

HOST = '192.168.0.69'    # The remote host
PORT = 8765              # The same port as used by the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
time.sleep(1)
for i in range(10):
    sock.sendall(encode.Encode())
    data = sock.recv(4096)
    print('Received', repr(data))
    print(encode.Decode(data).ledRGB)   