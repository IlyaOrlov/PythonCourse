import socket

my_dict = {
        '1': 'My',
        '2': 'name',
        '3': 'is',
        '4': 'Vasya',
}
lst = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12347
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    d = conn.recv(1024)
    d = d.decode()

    for i in d.split(' '):
        for j in my_dict.keys():
            if j == i:
                i = my_dict[j]
        lst.append(i)
    d = (' '.join(lst))
    conn.send(d.encode())
    conn.close()
# s.close()