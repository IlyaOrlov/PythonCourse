import socket
import pickle

data = ['first', 'second', 'third']
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(pickle.dumps(data), ('127.0.0.1', 12345))
print(*pickle.loads(s.recv(1024)))
s.close()