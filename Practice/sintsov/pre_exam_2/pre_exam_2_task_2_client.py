#2
import socket
import sys

class IterClient:
    def __init__(self, host, port, step=1):
        self.step, self.count = step, 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.data = self.sock.recv(1024)

    def __next__(self):
        data_size = sys.getsizeof(self.data) - 17 # не нашел нигде почему 17 байт прибавляется при encode()
        end_of_range = self.count + self.step if self.count + self.step <= data_size else data_size
        if self.count < data_size:
            bytes = self.data[self.count : end_of_range : 1]
            self.count = end_of_range
            return bytes
        else:
            self.sock.close()
            raise StopIteration

    def __iter__(self):
        return self


class IterClient_2:
    def __init__(self, host, port, step=1):
        self.step, self.count = step, 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def __next__(self):
        data = self.sock.recv(self.step)
        if data:
            return data
        self.sock.close()
        raise StopIteration

    def __iter__(self):
        return self


for i in IterClient_2('localhost', 4001, 3):
    print(i)
