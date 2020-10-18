import socket
import threading


class Handler:
    def __init__(self):
        pass

    def handle(self, word):
        return f"[{word}]"


class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server_socket = None
        self._running = True
        self.thread_conns = {}

    def run_server(self):
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Server run")
        while self._running:
            conn, addr = self.server_socket.accept()
            self.start_client_serving(conn, addr)

    def start_client_serving(self, conn, addr):
        thread = threading.Thread(target=self.serve_client, args=(conn, addr), name=f"client_servant-{conn.fileno()}")
        thread.start()
        self.thread_conns[thread.native_id] = conn

    def serve_client(self, conn, addr):
        servant_name = threading.current_thread().name
        initial_data = conn.recv(1024)
        print(f"{servant_name} connected with {addr}, initial data: {str(initial_data, 'utf-8')}")
        while True:
            request = conn.recv(1024)
            if request:
                str_request = str(request, "utf-8")
                print(f"{servant_name} receive: {str_request}")
                response = self.handler.handle(str(request, "utf-8"))
                print(f"{servant_name} is about answer: {response}")
                conn.send(response.encode())
            else:
                break
        print(f"{servant_name} disconnected with {addr}")
        conn.close()
        del self.thread_conns[threading.current_thread().native_id]

    def stop_server(self):
        self._running = False
        self.stop_threads()
        self.server_socket.close()
        print("Server stopped")

    def stop_threads(self):
        for thread in threading.enumerate():
            if thread.name.startswith("client_servant"):
                self.thread_conns[thread.native_id].shutdown(socket.SHUT_RDWR)


if __name__ == '__main__':
    handler = Handler()
    server = Server("localhost", 8000, handler)
    try:
        server.run_server()
    except KeyboardInterrupt:
        server.stop_server()
