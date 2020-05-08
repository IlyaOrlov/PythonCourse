import socket
import random
import pickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} y.o.'


class TcpClient:
    def __init__(self, host, port, user):
        self.host = host
        self.port = port
        self.user = user
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(pickle.dumps(self.user))


if __name__ == '__main__':
    names = ['John', 'Alex', 'Oliver', 'Jeff', 'David', 'Tim', 'George', 'Marc']
    client = TcpClient('127.0.0.1', 55555, User(random.choice(names), random.randint(18, 70)))
    client.run()
    while True:
        pass
