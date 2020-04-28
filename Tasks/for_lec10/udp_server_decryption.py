import socket


def decrypt(string):
    res = ""
    for x in string.split(' '):
        if x.isdigit():
            res += chr(int(x))
        else:
            res += x
    return res


# AF_INET соответствует адресам IPv4
# SOCK_DGRAM соответствует протоколу UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
while True:
    data, addr = s.recvfrom(1024) # размер буфера для данных – 1024 байта
    print('Server got data from client: {}'.format(decrypt(data.decode())))
    s.sendto('Thank you for the data'.encode(), addr)
# s.close()
