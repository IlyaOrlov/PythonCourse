import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost', 4001))
str = input('Введите закодированное послание: ')
sock.send(str.encode())
data = sock.recv(1024)
sock.close()

print ('Послание звучит так: {}'.format(data.decode()))