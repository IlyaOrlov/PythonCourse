import socket
from CesarShifr import decoder


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    getdata = data.decode().split('\n')
    key = 3
    print('Server got connection from {}'.format(addr))
    print('Server got message from client: {}'.format(data.decode()))
    conn.send(('Server got message from client: {} '
               '\nServer decode message: {}'.format(data.decode(),decoder(getdata[0]),key)).encode())

    print('Decoded message from client: {}'.format(decoder(getdata[0]),key))
    conn.close()