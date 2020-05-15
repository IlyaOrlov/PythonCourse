import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8787
s.bind((host, port))
s.listen(5)

r = "abcd"
while True:
    conn, addr = s.accept()
    conn.send(r.encode())
    conn.send('q'.encode())
    conn.close()