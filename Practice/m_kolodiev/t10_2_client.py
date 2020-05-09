import socket
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    users = {'Henry': 29, 'John': 50, 'Oliver': 33, 'Stanley': 27}
    for u in users:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 12345))
        s.send(pickle.dumps(User(u, users[u])))
