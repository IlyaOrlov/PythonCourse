class Socket:         # only for mock-test
    pass


class ClientTread:    # only for mock-test
    pass


socket = Socket()     # only for mock-test


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def run(self):
        #1
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 3
        self._socket.bind((self.host, self.port))

        # 4
        self._socket.listen(5)
        self._running = True
        print('Server is up')

        # 5
        while self._running:
            conn, addr = self._socket.accept()
            ClientTread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
