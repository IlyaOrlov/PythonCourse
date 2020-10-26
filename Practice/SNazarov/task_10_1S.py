import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server.bind((host, port))
server.listen(5)
key = {'M': 'My', 'N': 'name', 'I': 'is', 'T': 'Transmission', 'C': 'Control', 'P': 'Protocol'}

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    print(f'Client {addr} send: {"".join(data)}')
    res = []

    for i in data:
        value = key.get(i)
        if value is None:
            print("Wrong key!")
            conn.send("It's an incorrect key!".encode())
        else:
            res.append(value)

    conn.send((" ".join(res)).encode())
    conn.close()
server.close()


