from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    # обработчик GET запросов
    def do_GET(self):
        self.send_response(200)  # OK
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # собственно html сообщение
        self.wfile.write('Hello World!'.encode())


if __name__ == '__main__':
    port = 8080
    server = HTTPServer(('127.0.0.1', port), MyHandler)
    print('Started HTTP server on port: {}'.format(port))
    # бесконечно ожидаем входящие http запросы
    server.serve_forever()