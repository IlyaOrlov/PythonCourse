import socket

my_dictionary = {'TCP': 'Transmission Control Protocol', 'UDP': 'User Datagram Protocol',
                 'HTTP': 'Hypertext Transfer Protocol',
                 'HTTPS': 'HyperText Transfer Protocol Secure', 'IP': 'Internet Protocol',
                 'URL': 'Uniform Resource Locator',
                 'URI': 'Universal Resource Identifier', 'HTML': 'HyperText Markup Language',
                 'XML': 'eXtensible Markup Language'}


def decrypt(word):
    if word not in my_dictionary:
        return 'Sorry, there is not such word in dictionary!'
    return my_dictionary[word]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 55555
s.bind((host, port))
s.listen(10)

while True:
    connection, address = s.accept()
    print('Successful connection from {}'.format(address))
    response = connection.recv(1024)
    decoded_response = response.decode()
    print('Response is {}'.format(decoded_response))
    string_to_send = decrypt(decoded_response)
    print('Reply is {}'.format(string_to_send))
    connection.send(string_to_send.encode())
    connection.close()
s.close()
