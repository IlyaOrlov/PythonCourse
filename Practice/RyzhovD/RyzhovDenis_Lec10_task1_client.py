import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 55443

s.connect((host, port))

# encrypted =
encrypted_list = ['1202', 'Houston, we\'ve got a problem!']
encrypted_pickle = pickle.dumps(encrypted_list)

# send(pickle.dumps(a))
# Do not need to encode since it has been pickled already
s.send(encrypted_pickle)
decrypted = s.recv(1024)
print('\n --- Apollo earphones (got from server) ---')
for x in pickle.loads(decrypted):
    print('Houston: {}'.format(x))
