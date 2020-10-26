import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
what_to_ask_server = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'HTML', 'XML', 'IP', 'URL', 'URI']

host = '127.0.0.1'
port = 55555
s.connect((host, port))
string_to_send = random.choice(what_to_ask_server)
print('I ask to server what is {}?'.format(string_to_send))
s.send(string_to_send.encode())
request_1 = s.recv(1024)
print('Server tell me {}'.format(request_1.decode()))
s.close()
