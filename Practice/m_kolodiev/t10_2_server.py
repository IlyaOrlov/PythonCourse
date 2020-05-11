import socket
import pickle
from t10_2_client import User


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)

while True:
    conn, addr = s.accept()
    user = pickle.loads(conn.recv(1024))
    print(f'User {user.name}, {user.age} y.o. connected from {addr}')
