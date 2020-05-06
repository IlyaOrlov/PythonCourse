import socket

lst = ['пр2в1т ', 'м1ня ', 'з3вут ', 'Д1н2с ']
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
