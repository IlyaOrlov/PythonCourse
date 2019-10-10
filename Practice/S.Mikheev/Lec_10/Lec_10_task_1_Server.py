import socket
import re


def decoder(phrase, step):
    step = -step
    alphabet_en = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:-!'
    decod_phrase = ''
    for symbol in phrase:
        index = alphabet_en.find(symbol)
        new_index = step + index
        if step >= 0:
            while new_index >= len(alphabet_en):
                new_index -= len(alphabet_en)
            if new_index < len(alphabet_en):
                decod_phrase += alphabet_en[new_index]
        else:
            while new_index < -len(alphabet_en):
                new_index += len(alphabet_en)
            if new_index > -len(alphabet_en):
                decod_phrase += alphabet_en[new_index]
    return decod_phrase


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


