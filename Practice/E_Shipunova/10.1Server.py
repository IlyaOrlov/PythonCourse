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
    shifr = conn.recv(1024).decode()   # get shifr from client
    print(f'I got "{"".join(shifr)}" from client {addr}.')

    res = []
    inv_secret = {v: k for k, v in secret.items()}  # dictionary is invented
    for ch in shifr:
        try:
            res.append(inv_secret[ch])
        except KeyError:
            print("It's an incorrect shifr!!!")
            conn.send("It's an incorrect shifr!!! I don't know what is this".encode())

    conn.send((''.join(res)).encode())
    print("The code decrypted successfully.")
    conn.close()
server.close()
