import socket

def crypt(str):
    dict = {'a': '1','b': '2','c': '3','d': '4','e': '5'}
    for i in str:
        # print(i, dict.get(i))
        if dict.get(i) != None:
            str = str.replace(i, dict.get(i))
            # print (str)
    return str

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345
# отправляем сообщение серверу без установки соединения
message = 'client data'
s.sendto(crypt(message).encode(), (host, port))
# получаем ответ от сервера
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
