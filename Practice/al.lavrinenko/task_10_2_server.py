import socket
import pickle
from task_10_2_client import User


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen(3)
users = {}

while True:
    conn, address = s.accept()
    user = pickle.loads(conn.recv(1024))
    print(f'\nServer got connection from {address}, user: {user}')
    users[address] = user
    print('\nUsers on the server:')
    for address in users:
        print(f'{users[address]}, {address}')
