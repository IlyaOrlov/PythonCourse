import socket
import time


class Client:
    def __init__(self, host, port, id):
        self.id = id
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.send(f"Client-{self.id}".encode())

    def disconnect(self):
        self.client_socket.close()

    def action(self, word):
        self.client_socket.send(word.encode())
        response = self.client_socket.recv(1024)
        return str(response, "utf-8")


if __name__ == '__main__':
    id = int(time.time() * 1000) % 10000
    client = Client("localhost", 8000, id)
    client.connect()
    try:
        while True:
            answer = client.action(input("Enter a word: "))
            print(f"Server answer: {answer}")
    except KeyboardInterrupt:
        client.disconnect()
