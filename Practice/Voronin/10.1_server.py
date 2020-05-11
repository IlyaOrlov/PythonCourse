import socket

d = {'cat': 'кошка ', 'dog': 'собака ', 'mouse': 'мышь ', 'parrot': 'попугай '}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(1)
while True:
    conn, addr = s.accept()
    f = conn.recv(1024)
    f = f.decode()
    for x in d.keys():
        f = f.replace(x, d[x])

    conn.send(f.encode())
    conn.close()



