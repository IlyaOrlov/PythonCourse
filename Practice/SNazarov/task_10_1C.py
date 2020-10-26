import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client.connect((host, port))
client.send('MNITCP'.encode())
print(f'{client.recv(1024).decode()}')
client.close()
