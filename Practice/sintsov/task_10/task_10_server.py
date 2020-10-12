import socket

def translate(str):
    d = dict(zip(list('абвгдежзиклмнопрстуфхцчшщэюя'),
                 list('abvgdegziklmnoprstufhc466eya')))
    lst = []
    for c in str:
        lst.append(d.get(c) if d.get(c) else '*')
    return ''.join(lst)


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',4001))
sock.listen(1)
print("Server has started")
conn, addr = sock.accept()
print('Server got connection from {}'.format(addr))

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(translate(data.decode()).encode())
    break
conn.close()