import socket
import pickle
import random
import user


class TcpClient:
    def __init__(self, port, host):
        self.port = port
        self.host = host
        self._client = None

    def run(self):
        f_name = ['Andrey', 'Sergey', 'Roma', 'Yura', 'Oleg', 'Dmitriy', 'Ilya']
        l_name = ['Ivanov', 'Petrov', 'Sidorov', 'Kotov', 'Gorin', 'Socolov', 'Delov']
        auto = ['BMW', 'Audi', 'Nissan', 'Mercedes', 'Honda', 'Toyota', 'Lexus']
        profession = ['engineer', 'pilot', 'farmer', 'lawyer', 'businessman', 'actor', 'waiter']
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((self.host, self.port))
        self._client.send(pickle.dumps(user.User(random.choice(f_name), random.choice(l_name), random.randint(18, 55),
                                                  random.choice(auto), random.choice(profession))))
        self._client.close()


if __name__ == '__main__':
    client = TcpClient(port=12345, host='127.0.0.1')
    client.run()
