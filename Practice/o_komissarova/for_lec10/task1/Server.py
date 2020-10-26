import threading
import socket
import json


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr
        self.decode_dict = {
            'd': 'a',
            'e': 'b',
            'f': 'c',
            'g': 'd',
            'h': 'e',
            'i': 'f',
            'j': 'g',
            'k': 'h',
            'l': 'i',
            'm': 'j',
            'n': 'k',
            'o': 'l',
            'p': 'm',
            'q': 'n',
            'r': 'o',
            's': 'p',
            't': 'q',
            'u': 'r',
            'v': 's',
            'w': 't',
            'x': 'u',
            'y': 'v',
            'z': 'w',
            'a': 'x',
            'b': 'y',
            'c': 'z'
        }

    def run(self):
        print('Connection from address {}'.format(self._address))
        data = self._connection.recv(1024).decode()
        encoded_list = json.loads(data)
        decoded_list = []
        for word in encoded_list:
            decoded_word = ''
            for i in word:
                decoded_word += self.decode_dict[i]
            decoded_list.append(decoded_word)
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

    def stop(self):
        self._runnning = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = Server(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()

