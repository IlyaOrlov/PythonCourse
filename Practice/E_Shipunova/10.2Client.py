import socket
import pickle
import random
import time
import user

class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        names = ["Noah", "Mason", "Liam", "Alex", "Jack", "Harry", "Oscar", "Jacob"]
        position = ["baker", "poet", "butcher", "cook", "doctor", "engineer", "farmer", "pilot"]

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        time.sleep(5)
        self._socket.send(pickle.dumps(user.User(random.choice(names), random.randint(0, 99), random.choice(position))))
        self._socket.close()


if __name__ == "__main__":
    my_client = TcpClient(host = '127.0.0.1', port=5555)
    my_client.run()
