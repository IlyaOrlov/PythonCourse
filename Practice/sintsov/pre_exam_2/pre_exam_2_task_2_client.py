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
        if self.count < data_size:
            lst = []
            for i in range(self.count, self.count + self.step if self.count + self.step <= data_size else data_size):
                lst.append(bin(self.data[i])[2:])
            self.count = self.count + self.step if self.count + self.step <= data_size else data_size
            return "".join(lst)
        else:
            self.sock.close()
            raise StopIteration

    def __iter__(self):
        return self


for i in IterClient('localhost', 4001, 2):
    print(i)
