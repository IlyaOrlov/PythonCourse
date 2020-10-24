import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',4001))
sock.listen(1)
print("Server has started")
line = input("Введите сообщение: ")
conn, addr = sock.accept()
print('Server got connection from {}'.format(addr))
conn.send(line.encode())
conn.close()