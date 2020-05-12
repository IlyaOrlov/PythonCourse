import socket


class IterClient:
    def __init__(self, host, port, num=1):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.length = int(self.s.recv(1).decode())
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.length > 0:
           res = self.s.recv(self.num).decode()
           self.length -= self.num
           return res
        else:
            raise StopIteration


for i in IterClient('192.168.56.102', 12345):
    print(i)