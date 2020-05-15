import socket

lst = ['cat', 'dog', 'mouse', 'parrot']
a = ""
for i in lst:
    a += str(i)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
s.send(a.encode())
f = s.recv(1024)
f = f.decode()
print(f)
s.close()
