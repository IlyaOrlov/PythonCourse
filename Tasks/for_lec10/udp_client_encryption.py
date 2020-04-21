import socket

def encrypt(string):
    res = ""
    for x in string:
        res += str(ord(x)) + ' '
    return res

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
# отправляем сообщение серверу без установки соединения
s.sendto(encrypt('hello world').encode(), (host, port))
# получаем ответ от сервера
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
