import socket
import pickle


def decrypt(enc_words):
    return [dec_dict[word] for word in enc_words]


dec_dict = {'first': 'one', 'second': 'two', 'third': 'three'}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 12345))

while True:
    data, address = s.recvfrom(1024)
    s.sendto(pickle.dumps(decrypt(pickle.loads(data))), address)