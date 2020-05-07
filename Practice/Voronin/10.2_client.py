import socket

class Users:
    def __init__(self, host, port, name, age):
        self.host = host
        self.port = port
        self.name = name
        self.age = age
        self.socket = None
    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.send(self.name.encode())
        self.socket.send(self.age.encode())
        self.socket.close()

# ivan = Users('127.0.0.1', 8787, 'Ivan', ' 37')
# ivan.run()
sergei = Users('127.0.0.1', 8787, 'Sergei', ' 21')
sergei.run()


