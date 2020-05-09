import socket
import pickle

class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ivan = Users('Ivan', ' 37')
sergei = Users('Sergei', ' 21')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8787
s.connect((host, port))
s.send(pickle.dumps(sergei))
s.close()
