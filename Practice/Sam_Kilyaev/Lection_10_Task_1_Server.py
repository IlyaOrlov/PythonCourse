import socket


secret = {'I': 'I', 'M': 'am', 'B': 'work', 'N': '!!!'}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server.bind((host, port))
server.listen(5)
while True:
    conn, addr = server.accept()
    code = conn.recv(1024).decode()
    print(f'I get"{"".join(code)}" from client {addr}.')
    result = []
    for i in code:
        try:
            a = secret.get(i)
            result.append(a)
        except KeyError:
            print("I don't know")
            conn.send("What do you mean?".encode())
    for j in result:
        if j == None:
            result = []
    conn.send((''.join(result)).encode())
    conn.close()
server.close()
