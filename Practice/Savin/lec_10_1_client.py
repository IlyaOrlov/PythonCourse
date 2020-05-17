import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 12345))
words = ['dog', 'cat', 'tiger']
for word in words:
    sock.send((word + ' ').encode())
message = sock.recv(1024)
print(f'Полученное сообщение с сервера: {message.decode()}')
sock.close()