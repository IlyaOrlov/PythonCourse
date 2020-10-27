import json
import socket
import base64


class Client:
    def __init__(self, host, port, encoded_words):
        self.port = port
        self.host = host
        self.encoded_words = encoded_words
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(json.dumps(self.encoded_words).encode())
        data = self._socket.recv(1024).decode()
        result_list = json.loads(data)
        print('Received: {}'.format(result_list))
        self._socket.close()


if __name__ == '__main__':
    encoded_words = ['dafadvsdh', 'aaadsdw']
    new_client = Client('127.0.0.1', 5555, encoded_words)
    new_client.run()
