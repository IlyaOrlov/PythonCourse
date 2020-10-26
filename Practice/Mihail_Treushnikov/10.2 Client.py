import pickle
import socket
from second.user import User


class Client:
    def __init__(self, host, port, user):
        self.port = port
        self.host = host
        self._user = user
        self._socket = None

    @property
    def user(self):
        return self._user

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        sss = pickle.dumps(self.user, protocol=pickle.HIGHEST_PROTOCOL)
        self._socket.send(sss)
        self._socket.close()


if __name__ == '__main__':
    user1 = User("User1", "25")
    user2 = User("User2", "21")
    cl1 = Client('127.0.0.1', 5555, user1)
    cl1.run()
    cl2 = Client('127.0.0.1', 5555, user2)
    cl2.run()
