import socket
import pickle

CIPHER_BOOK = {'1202': 'We\'re GO on that alarm.',
               'Houston, we\'ve got a problem!': 'Failure is not an option!'}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 55443
s.bind((host, port))
s.listen(5)
while True:  # server listens in infinite loop
    conn, addr = s.accept()
    # print('Server got connection from {}'.format(addr))  ##
    # print(conn)  ##
    encrypted_recvd = pickle.loads(conn.recv(1024))
    decrypted = []
    print('\n --- Houston earphones (got from client) ---')
    for z in encrypted_recvd:
        print('Apollo: {}'.format(z))
        decrypted.append(CIPHER_BOOK[z])
    decrypted_pickle = pickle.dumps(decrypted)
    conn.send(decrypted_pickle)
    # if
    conn.close()  # here we close connection

s.close()  # if loop is not infinite close server
