import socket
import pickle
from users import Users

ivan = Users('Ivan', '37')
sergei = Users('Sergei', '21')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8787
s.connect((host, port))
s.send(pickle.dumps(ivan))
s.close()
