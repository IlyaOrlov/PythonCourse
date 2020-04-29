import socket
import pickle

from lec_10_2_user import User


class TcpClient:
    def __init__(self, host: str, port: int, user: User):
        self.user = user
        self.port = port
        self.host = host
        self._socket = None


    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        message = pickle.dumps(self.user)
        self._socket.send(message)
        self._socket.close()


if __name__ == '__main__':
    u1 = User('Tom', 25)
    u2 = User('Frank', 30)
    u3 = User('Alex', 20)

    clients = [u1, u2, u3]

    for client in clients:
        myclient = TcpClient(host='192.168.0.13', port=9090, user=client)
        myclient.run()
