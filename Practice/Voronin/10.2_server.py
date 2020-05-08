import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8787
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    f = conn.recv(1024)
    with open('data.pickle', 'rb') as d:
        d_new = pickle.load(d)
    print(d_new)
    conn.close()