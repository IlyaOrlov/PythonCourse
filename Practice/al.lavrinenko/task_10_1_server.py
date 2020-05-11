import socket
import pickle


def decrypt(enc_words):
    return [dec_dict[word] for word in enc_words]


dec_dict = {'one': 'first', 'two': 'second', 'three': 'third'}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 55555))

while True:
    data, address = s.recvfrom(1024)
    s.sendto(pickle.dumps(decrypt(pickle.loads(data))), address)
