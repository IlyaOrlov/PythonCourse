import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',4001))
sock.listen(1)
print("Server has started")
line = input("Введите сообщение: ")
data = line.encode()
conn, addr = sock.accept()
print('Server got connection from {}'.format(addr))

conn.send(data)
conn.close()