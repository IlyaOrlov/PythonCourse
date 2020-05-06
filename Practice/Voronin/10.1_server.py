import socket

dict = {'0': 'а', '1': 'е', '2': 'и', '3': 'о'}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
while True:
    f = conn.recv(1024)
    f = f.decode()
    a = ''
    for x,i in enumerate(f):
        if i == '0':
            a += dict[i]
        elif i == '1':
            a += dict[i]
        elif i == '2':
            a += dict[i]
        elif i == '3':
            a += dict[i]
        else:
            a += f[x]
    conn.send(a.encode())
    conn.close()



