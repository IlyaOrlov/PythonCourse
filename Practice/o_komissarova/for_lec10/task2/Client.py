import pickle
import socket
from Practice.o_komissarova.for_lec8.task9 import User


class Client:
    def __init__(self, host, port, user):
        self.host = host
        self.port = port
        self.user = user
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(pickle.dumps(self.user))
        self._socket.close()


if __name__ == '__main__':
    user_John = User('John', 25)
    user_Jack = User('Jack', 30)
    my_client1 = Client('127.0.0.1', 5555, user_John)
    my_client1.run()
    my_client2 = Client('127.0.0.1', 5555, user_Jack)
    my_client2.run()
