import socket
import time
from cryptography.fernet import Fernet


def encrypt(msg):
    key = b'5_RIkwkfPKcQQNmAlffhqNEg-4_wUUEkQMnF8OUOpJQ='
    cipher = Fernet(key)
    encrypted_msg = cipher.encrypt(msg.encode())
    return encrypted_msg


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 12345
messages = ['Wake up, Neo...', 'The Matrix has you...', 'Follow the white rabbit.', 'Knock, knock, Neo.']
for message in messages:
    s.sendto(encrypt(message), (host, port))
    time.sleep(3)
data, addr = s.recvfrom(1024)
print(data.decode())
s.close()
