import threading
import socket
import datetime
import pickle


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        data = self._connection.recv(1024)
        user = pickle.loads(data)
        print(f'User {user.name}, age {user.age} connected in {datetime.datetime.now().strftime("%H:%M:%S")}')
        while True:
            a = self._connection.recv(1024)
            if a.decode() == 'quit':
                self._connection.close()
                print(f'User {user.name} disconnected in {datetime.datetime.now().strftime("%H:%M:%S")}')
                break
            else:
                print(f'{user.name}: {a.decode()}')


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
        print(f'Server up in {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print(f'Server down in {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
