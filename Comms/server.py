import socket

class Receiveclass:
    data = ''
    HOST = 0
    PORT = 0
    def Initialize(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.HOST, self.PORT))
        s.listen(1)
        print("elo")
        while True:
            conn, addr = s.accept()
            i=1
            print('Connected by', addr)
            while i==1:
                self.data = conn.recv(4096)
                #print(recv)
                if not conn.recv: i=0


        
            
