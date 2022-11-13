import socket
from time import sleep
# class Receiveclass:
#     data = ''
#     HOST = ''
#     PORT = 0
#     def Initialize(self):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind((self.HOST, self.PORT))
#         print("elo")
#         while True:
#             s.listen(1)
#             conn, addr = s.accept()
#             i=1
#             print('Connected by', addr)
#             while i==1:
#                 self.data = conn.recv(4096)
#                 if not conn.recv: i=0
class DataHold:
    data = '0'
datahold = DataHold()
datahold.data = '0'

def Initialize(PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.0.15', PORT))
    print(f"elo, {s.getsockname()}")
    while True:
        s.listen(1)
        conn, addr = s.accept()
        i=1
        print('Connected by', addr)
        while i==1:
            datahold.data = conn.recv(4096)
            if not conn.recv:
                i=0

    
