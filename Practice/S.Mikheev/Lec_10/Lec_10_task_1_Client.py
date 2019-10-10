import socket
from ciphercaesar import encoder

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))
a = 'Hello, world!'
step = 45  # Шаг, он же ключ для шифровки
s.send(
    (encoder(a, step) + '\n' + 'Key for decode: {}'.format(step)).encode())  # Передаем зашифрованное сообщение и ключ
# Предполагается, что у сервера есть дешифровщик
d = s.recv(1024)
print(d.decode())
s.close()

