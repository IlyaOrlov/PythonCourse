import socket

host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send('123456_37_8_905.4-'.encode())
print(f'i got "{client.recv(1024).decode()}" from server.')

client.close()
