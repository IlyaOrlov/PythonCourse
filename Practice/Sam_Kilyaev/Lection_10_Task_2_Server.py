import socket
import pickle
import threading
from Lection_7_Task_3 import Human

class ClientThread(threading.Thread):

    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        b = self._connection.recv(1024)
        a = pickle.loads(b)
        print(f'My address is {self._address}, my name {a}')
        self._connection.close()


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()


if __name__ == "__main__":
    srv = TcpServer(host='127.0.0.1', port=12345)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()