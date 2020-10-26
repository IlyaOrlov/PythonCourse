import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
dictionary = {
           'c': '1',
           'l': '2',
           'i': '3',
           'e': '4',
           'n': '5',
           't': '6',
           's': '7',
           'a': '8',
           'd': '9',
           'o': '0',
           'k': '.',
           'y': '-',
           ' ': '_'
           }

server.bind((host, port))
server.listen(1)

while True:
    conn, addr = server.accept()
    code = conn.recv(1024).decode()
    print(f'Server catch "{"".join(code)}" from {addr}.')

    res = []
    inv_dictionary = {v: k for k, v in dictionary.items()}
    for symbol in code:
        try:
            res.append(inv_dictionary[symbol])
        except KeyError:
            print("error")

    conn.send((''.join(res)).encode())
    print("done. view answer on client")
    conn.close()
server.close()
