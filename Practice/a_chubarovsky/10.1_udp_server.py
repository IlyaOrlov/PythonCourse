import socket
from cryptography.fernet import Fernet
import datetime


def decrypt(msg):
    key = b'5_RIkwkfPKcQQNmAlffhqNEg-4_wUUEkQMnF8OUOpJQ='
    cipher = Fernet(key)
    return cipher.decrypt(msg).decode()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 12345
print(f'Server up in {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
s.bind((host, port))
rcvd_data = []
while True:
    data, addr = s.recvfrom(1024)
    print(f'{datetime.datetime.now().strftime("%H:%M:%S")}: {decrypt(data)}')
    rcvd_data.append(decrypt(data))
    if len(rcvd_data) == 4:
        s.sendto(f'Received messages from client: {rcvd_data}'.encode(), addr)
