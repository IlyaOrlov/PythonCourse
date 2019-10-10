import socket
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


users = {'Sergei': 30, 'Alex': 20, 'Gennadiy': 45}
for user in users:
    p = pickle.dumps(User(user, users[user]), protocol=pickle.HIGHEST_PROTOCOL)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))
    s.send(p)
    d = s.recv(1024)
    print(d.decode())
    s.close()
