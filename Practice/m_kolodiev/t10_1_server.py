import socket
import json

dic = {'USD': 'dollars', 'EUR': 'euros', 'RUB': 'rubles'}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(5)

while True:
    conn, addr = s.accept()
    rec = json.loads(conn.recv(1024))
    dec_data = [dic[word] for word in rec]
    conn.send(json.dumps(dec_data).encode())
