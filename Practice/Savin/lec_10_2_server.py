import socket
import socketserver

from lec_10_2_user import User

host = socket.gethostbyname(socket.gethostname())
port = 9090


class TCPHandler(socketserver.BaseRequestHandler):

    clients = {}

    def handle(self):
        data = self.request.recv(1024).strip()
        addr = self.client_address[1]
        if addr not in self.clients:
            name, age = data.decode().split(' ')
            u = User(name, age)
            self.clients[addr] = u
            print(f'user {u.name} ({u.age} age) is connected. Address {addr}')


if __name__ == '__main__':
    with socketserver.TCPServer((host, port), TCPHandler) as server:
        server.serve_forever()
