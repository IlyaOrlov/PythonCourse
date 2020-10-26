import socket

host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send('IMBN'.encode())
print(f'{client.recv(1024).decode()}')

client.close()
