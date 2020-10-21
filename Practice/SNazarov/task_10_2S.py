import socket
import pickle
import threading


class ClientThread(threading.Thread):

    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        response = self._connection.recv(1024)
        data_res = pickle.loads(response)
        print(f'Client {self._address} send: {data_res}')
        self._connection.close()


class TcpServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._server = None
        self._running = False

    def run(self):
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind((self.host, self.port))
        self._server.listen(5)
        self._running = True

        while self._running:
           conn, addr = self._server.accept()
           ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._server.close()


if __name__ == '__main__':
    server = TcpServer(host='127.0.0.1', port=12345)
    try:
        server.run()
    except KeyboardInterrupt:
        server.stop()
