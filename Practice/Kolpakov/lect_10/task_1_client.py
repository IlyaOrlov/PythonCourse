import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12347
s.connect((host, port))
s.send('1 2 3 4'.encode())
d = s.recv(1024)
print(d.decode())

s.close()