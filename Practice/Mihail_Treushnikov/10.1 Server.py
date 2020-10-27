import json
import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr
        self._dec_dict = {"h": "привет", "w": "мир"}

    def run(self):
        print('Connection from address {}'.format(self._address))
        enc = self._connection.recv(1024).decode()
        encoded_list = json.loads(enc)
        decoded_list = []
        for i in encoded_list:
            for j in i:
                if j=="h":
                    decoded_list.append(self._dec_dict.get("h"))
                elif j =="w":
                    decoded_list.append(self._dec_dict.get("w"))
        print('Received {}'.format(encoded_list))
        print('Decoded {}'.format(decoded_list))
        self._connection.send(json.dumps(decoded_list).encode())
        self._connection.close()
        print('Closed connection from {}'.format(self._address))


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._runnning = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._runnning = True
        print('Server is up')
        while self._runnning:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()


if __name__ == '__main__':
    srv = Server(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
