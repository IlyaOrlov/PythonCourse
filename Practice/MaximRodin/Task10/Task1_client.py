import socket
from CesarShifr import encoder

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
msg = 'Привет мир'
step = 3  # ключ шифровки
s.send((encoder(msg, step) + '\n' + 'Key: {}'.format(step)).encode())

d = s.recv(1024).decode()
print(d)
s.close()