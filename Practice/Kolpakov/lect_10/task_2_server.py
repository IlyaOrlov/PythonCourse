import socket
import pickle

class User:
    def __init__(self, user_name, user_age):
        self.user_name = user_name
        self.user_age = user_age
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12341
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    d = conn.recv(1024)
    d = pickle.loads(d)
    print(f'Server got connection from {addr}, name: {d.user_name}, age: {d.user_age}')
    conn.close()
# s.close()