import socket

d = {'0': 'а', '1': 'е', '2': 'и', '3': 'о'}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
while True:
    f = conn.recv(1024)
    f = f.decode()
    for x in d.keys():
        f = f.replace(x, d[x])

    conn.send(f.encode())
conn.close()



