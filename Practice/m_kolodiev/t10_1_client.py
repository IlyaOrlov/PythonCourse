import socket
import json

data = ['USD', 'EUR', 'RUB']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
s.send(json.dumps(data).encode())

rec = s.recv(1024).decode()
print(', '.join(json.loads(rec)))
s.close()
