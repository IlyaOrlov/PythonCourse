import socket
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    user = pickle.loads(data)
    print('Server got connection from {}'.format(addr))
    print('New user connected: {}, age: {}'.format(user.name, user.age))
    conn.send('Thank you for the connection, Server identified user: {}'.format(user.name).encode())
    conn.close()
