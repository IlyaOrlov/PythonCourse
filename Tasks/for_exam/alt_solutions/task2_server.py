import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
str_to_send = "abcd"
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    conn.send(str(len(str_to_send)).encode())
    conn.send(str_to_send.encode())
    conn.close()
s.close()
