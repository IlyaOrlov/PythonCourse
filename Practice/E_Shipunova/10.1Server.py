import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # internet, TCP
host = '127.0.0.1'   # locale host
port = 12345
secret = {
           'I': '.',
           'a': '*',
           'm': 'P',
           ' ': '$',
           'r': 'q',
           'e': ':',
           'd': '-',
           'i': ')',
           'n': '%',
           'h': '#',
           'g': ',',
           't': '!',
           'x': '>'
           }

server.bind((host, port))
server.listen(5)

while True:
    conn, addr = server.accept()
    shifr = list(conn.recv(1024).decode())  # get shifr from client
    print(f'I got "{"".join(shifr)}" from client {addr}.')

    res = []
    for ch in shifr:
        for key in secret.keys():
            if ch == secret[key]:
                res.append(key)

    conn.send((''.join(res)).encode())
    conn.close()
server.close()
