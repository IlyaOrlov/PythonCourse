import socket

def encrypt(str):
    dict = {'a': '1','b': '2','c': '3','d': '4','e': '5'}
    dict1 = {}
    for z in dict:
        # print(z, dict.get(z))
        dict1.update({dict.get(z):z})
        # print(dict1)
    for i in str:
        # print(i, dict.(i))
        if dict1.get(i) != None:
            str = str.replace(i, dict1.get(i))
            # print (str)
    return str
# AF_INET соотвествует адресам IPv4
# SOCK_DGRAM соотвествует протоколу UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345
s.bind((host, port))
while True:
    data, addr = s.recvfrom(1024)
    print('Server got data from client: {}'.format(encrypt(data.decode())))
    s.sendto('Thank you for the data'.encode(), addr)
# s.close()
