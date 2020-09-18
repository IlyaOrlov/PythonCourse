import socket

host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send('.$*P$q:*-)%,$!#:$!:>!'.encode())  # for testing incorrect shifr: '.$*PB$q:*-$!:>!'.encode()
print(f'I got "{client.recv(1024).decode()}" from server.')

client.close()
