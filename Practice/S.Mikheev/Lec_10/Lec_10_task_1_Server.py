import re
import socket
from ciphercaesar import decoder


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    inbox = data.decode().split('\n')  # Получаем данные и преобразуем их в список по разделителю
    key = re.search(r'Key for decode: (\b\d+\b)', data.decode())  # Вытаскиваем ключ для расшифровки сообщения
    print('Server got connection from {}'.format(addr))
    print('Server got data from client: {}'.format(data.decode()))
    conn.send(('Thank you for the connection, Server got data from client: {}'
               '\nServer decode data: {}'.format(data.decode(), decoder(inbox[0], int(key.group(1))))).encode())
    print('Server got data from client and decode it: {}'.format(decoder(inbox[0], int(key.group(1)))))
    conn.close()


