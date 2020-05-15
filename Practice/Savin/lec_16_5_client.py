import socket, pickle


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 12345))
sock.send('ID=1'.encode())
message = pickle.loads(sock.recv(1024))
print(f'Полученное сообщение с сервера: {message}')
sock.close()