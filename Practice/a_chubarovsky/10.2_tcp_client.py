import socket
import pickle
from user_info import User


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        print(f'Connected to server: host - {self.host}, port - {self.port}.')
        user = User(name=input('Enter your name: '), age=int(input('Enter your age: ')))
        self._socket.send(pickle.dumps(user, protocol=pickle.HIGHEST_PROTOCOL))
        while True:
            a = input()
            self._socket.send(f'{a}'.encode())
            if a == 'quit':
                self._socket.close()
                break


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5555
    my_tcp_client = TcpClient(host, port)
    my_tcp_client.run()
