import threading
import socket
import pickle


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        print('Successful connection from {}'.format(self._address))
        data = pickle.loads(self._connection.recv(1024))
        print('Received {}'.format(data))
        self._connection.close()
        print('Closed connection from {}'.format(self._address))


class TCPServer:
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
        print('Server is started')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print('Server is stopped')


if __name__ == '__main__':
    my_server = TCPServer(host='127.0.0.1', port=3333)
    try:
        my_server.run()
    except KeyboardInterrupt:
        my_server.stop()
