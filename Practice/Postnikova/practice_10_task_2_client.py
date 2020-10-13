import socket
import random
import pickle
import user


class TCPClient:
    def __init__(self, host, port, name):
        self._host = host
        self._port = port
        self.name = name
        self._socket = None

    def run(self, some_user):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._host, self._port))
        self._socket.send(pickle.dumps(some_user))
        print('I have send {}'.format(some_user))
        self._socket.close()


def create_user():
    names = ['Фёдор', 'Василиса', 'Марк', 'Марфа', 'Никодим']
    ages = [89, 78, 85, 72, 99]
    return user.User(random.choice(names), random.choice(ages))


if __name__ == '__main__':
    name = 'Client'
    my_client = TCPClient(host='127.0.0.1', port=3333, name=name)
    my_client.run(create_user())
