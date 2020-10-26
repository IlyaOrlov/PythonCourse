import socket
import json


class Client:
    def __init__(self, host, port, encoded_list):
        self.host = host
        self.port = port
        self.encoded_list = encoded_list
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(json.dumps(self.encoded_list).encode())
        data = self._socket.recv(1024).decode()
        decoded_list = json.loads(data)
        print('Received: {}'.format(decoded_list))
        self._socket.close()


if __name__ == '__main__':
    encoded_list = ['pdqb', 'gliihuhqw', 'zrugv']
    my_client = Client('127.0.0.1', 5555, encoded_list)
    my_client.run()
