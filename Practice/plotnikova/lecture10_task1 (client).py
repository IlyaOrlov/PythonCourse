import socket
import random


class TcpClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name =name
        self.received = None
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(self.my_send().encode())
        print('Send: {}'.format(self.name))
        data = self._socket.recv(1024)
        print('Received: {}'.format(data.decode()))
        self._socket.close()

    def my_send(self):
        if isinstance( self.name, list):
            self.name = ",".join(name)
        return  self.name


if __name__ == '__main__':
    name = ["1", "2", "3","4", "5", "6"]
    myclient = TcpClient(host='127.0.0.1', port=5555, name=name)
    myclient.run()