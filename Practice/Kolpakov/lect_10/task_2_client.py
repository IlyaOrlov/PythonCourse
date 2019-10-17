import socket
import pickle

class User:
    def __init__(self, user_name, user_age):
        self.user_name = user_name
        self.user_age = user_age

user1 = pickle.dumps(User('Ivan', 25))
user2 = pickle.dumps(User('Vasya', 65))
user3 = pickle.dumps(User('Grigoriy', 34))
users = [user1, user2, user3]

for user in users:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12341
    s.connect((host, port))
    s.send(user)
    s.close()

