import socket
import pickle

data = ['two', 'one', 'three']
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(pickle.dumps(data), ('127.0.0.1', 55555))
print(*pickle.loads(s.recv(1024)))
s.close()
