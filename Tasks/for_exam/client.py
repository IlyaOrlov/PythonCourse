import socket
import pickle


class IterClient:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 8787
        self.s.connect((host, port))
    def __iter__(self):
        return self
    def __next__(self):
        res = self.s.recv(1).decode()
        if res != 'q':
            return res
        self.s.close()
        raise StopIteration


for i in IterClient():
    print(i)

