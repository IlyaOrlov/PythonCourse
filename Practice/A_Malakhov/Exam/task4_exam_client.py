import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
data = s.send('Hello'.encode())
ret_data = s.recv(1024)
print(ret_data.decode())
s.close()
