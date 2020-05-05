import socket

d = {'dog': 'собака', 'cat': 'кошка', 'tiger': 'тигр'}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 12345))
sock.listen(5)
while True:
    client, addr = sock.accept()
    message = client.recv(1024)
    print(f'Полученное сообщение от клиента: {message.decode()}')
    words_eng = message.decode().split()
    words_ru = [d[word] for word in words_eng]
    result = ' '.join(words_ru)
    client.send(result.encode())
    client.close()