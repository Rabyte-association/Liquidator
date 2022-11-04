import socket

HOST = '192.168.0.69'                 # Symbolic name meaning all available interfaces
PORT = 8765              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            if not data: break
            conn.sendall(data)