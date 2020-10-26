import socket


class Handler:
    def __init__(self):
        self.decoder = {"hello": "bye",
                   "morning": "evening",
                   "front": "back"}

    def handle(self, word):
        return self.decoder.get(word, "unknown word")


class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server_socket = None
        self._running = True

    def run_server(self):
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Server run")
        while self._running:
            conn, addr = self.server_socket.accept()
            print(f"I've connected with {addr}")
            self.serve_client(conn)
            print(f"I've disconnected with {addr}")
            conn.close()

    def serve_client(self, conn):
        while True:
            request = conn.recv(1024)
            if request:
                str_request = str(request, "utf-8")
                print(f"I receive: {str_request}")
                response = self.handler.handle(str(request, "utf-8"))
                print(f"I'm about answer: {response}")
                conn.send(response.encode())
            else:
                break

    def stop_server(self):
        self._running = False
        self.server_socket.close()
        print("Server stopped")


if __name__ == '__main__':
    handler = Handler()
    server = Server("localhost", 8000, handler)
    try:
        server.run_server()
    except KeyboardInterrupt:
        server.stop_server()
