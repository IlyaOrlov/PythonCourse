import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345
# отправляем сообщение серверу без установки соединения
s.sendto('client data'.encode(), (host, port))
# получаем ответ от сервера
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()