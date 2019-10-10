import socket


def encoder(phrase, step):  # Буду использовать для шифровки сообщений "Шифр Цезаря"
    alphabet_en = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:-!'
    phrase = phrase.strip(' ')
    encod_phrase = ''
    for symbol in phrase:
        index = alphabet_en.find(symbol)
        new_index = step + index
        if step >= 0:
            while new_index >= len(alphabet_en):
                new_index -= len(alphabet_en)
            if new_index < len(alphabet_en):
                encod_phrase += alphabet_en[new_index]
        else:
            while new_index < -len(alphabet_en):
                new_index += len(alphabet_en)
            if new_index > -len(alphabet_en):
                encod_phrase += alphabet_en[new_index]
    return encod_phrase


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

