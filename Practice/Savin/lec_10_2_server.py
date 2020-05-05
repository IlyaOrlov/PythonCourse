import socket
import socketserver
import pickle


host = socket.gethostbyname(socket.gethostname())
port = 9090


class TCPHandler(socketserver.BaseRequestHandler):

    users = {}


    def handle(self):
        users = pickle.loads(self.request.recv(1024).strip())
        addr = self.client_address[1]
        if addr not in self.users:
            self.users[addr] = users
            print(f'user {users.name} ({users.age} age) is connected. Address {addr}')


if __name__ == '__main__':
    with socketserver.TCPServer((host, port), TCPHandler) as server:
        server.serve_forever()
