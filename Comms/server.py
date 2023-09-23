import socket
from time import sleep
# class Receiveclass:
#      data = ''
#      HOST = ''
#      PORT = 0
#      def Initialize(self):
#          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#          s.bind((self.HOST, self.PORT))
#          print("elo")
#          while True:
#              s.listen(1)
#              conn, addr = s.accept()
#              i=1
#              print('Connected by', addr)
#              while i==1:
#                  self.data = conn.recv(4096)
#                  if not conn.recv: i=0
class DataHold:
    data = '0'
datahold = DataHold()

def Initialize(PORT):
    datahold.data = b'\x80\x04\x95\x9e\x00\x00\x00\x00\x00\x00\x00\x8c\x13Comms.encode_client\x94\x8c\x06Struct\x94\x93\x94)\x81\x94}\x94(\x8c\x08hvbSpeed\x94K\x00\x8c\x06hvbDir\x94K\x00\x8c\x07HVB_ARM\x94K\x00\x8c\x03led\x94K\x00\x8c\nendstopOvr\x94K\x00\x8c\x06homing\x94K\x00\x8c\x06motorY\x94K\x00\x8c\x06motorZ\x94K\x00\x8c\x07motorX1\x94K\x00\x8c\x07motorX2\x94K\x00ub.'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.0.3', PORT))
    print(f"elo, {s.getsockname()}")
    while True:
        s.listen()
        conn, addr = s.accept()
        print('Connected by', addr)
        while True:
            try:
                datahold.data = conn.recv(4096)
                if datahold.data == b'':
                    break
            except:
                print('server error')
                break
        datahold.data = b'\x80\x04\x95\x9e\x00\x00\x00\x00\x00\x00\x00\x8c\x13Comms.encode_client\x94\x8c\x06Struct\x94\x93\x94)\x81\x94}\x94(\x8c\x08hvbSpeed\x94K\x00\x8c\x06hvbDir\x94K\x00\x8c\x07HVB_ARM\x94K\x00\x8c\x03led\x94K\x00\x8c\nendstopOvr\x94K\x00\x8c\x06homing\x94K\x00\x8c\x06motorY\x94K\x00\x8c\x06motorZ\x94K\x00\x8c\x07motorX1\x94K\x00\x8c\x07motorX2\x94K\x00ub.'


    
