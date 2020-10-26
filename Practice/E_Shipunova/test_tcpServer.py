import unittest
import mock
import tcpServer


class TestTcpServer(unittest.TestCase):

    server = tcpServer.TcpServer('127.0.0.1', 5555)

    def test_init_tcp_server(self):
        self.assertEqual('127.0.0.1', self.server.host)
        self.assertEqual(5555, self.server.port)
        self.assertIsNone(self.server._socket)
        self.assertFalse(self.server._running)

    @mock.patch('tcpServer.ClientTread')
    def test_run(self, ClientMock):                                 # change ClientTread-class to Mock-class
        with mock.patch('tcpServer.socket') as socket_mock:
            # for 1
            socket_mock.AF_INET = 'socket.AF_INET'
            socket_mock.SOCK_STREAM = 'socket.SOCK_STREAM'
            socket_mock.socket.return_value = socket_mock           # for next calls

            # for 2
            socket_mock.SOL_SOCKET = 'socket.SOL_SOCKET'
            socket_mock.SO_REUSEADDR = 'socket.SO_REUSEADDR'

            # for 5
            socket_mock.accept.side_effect = [('conn1', 'addr1'), ('conn2', 'addr2'), KeyboardInterrupt]
            client_mock_for_start = mock.Mock()
            ClientMock.return_value = client_mock_for_start         # for next calls with start()

            try:
                self.server.run()
            except KeyboardInterrupt:                               # for the third element of side_effect
                self.server.stop()

            # 1
            self.assertTrue(socket_mock.socket.called)
            socket_mock.socket.assert_called_once_with('socket.AF_INET', 'socket.SOCK_STREAM')
            # 2
            self.assertTrue(socket_mock.setsockopt.called)
            socket_mock.setsockopt.assert_called_once_with('socket.SOL_SOCKET', 'socket.SO_REUSEADDR', 1)
            # 3
            self.assertTrue(socket_mock.bind.called)
            socket_mock.bind.assert_called_once_with(('127.0.0.1', 5555))
            # 4
            self.assertTrue(socket_mock.listen.called)
            socket_mock.listen.assert_called_once_with(5)
            # 5
            assert ClientMock is tcpServer.ClientTread
            assert socket_mock.accept.call_count == 3                 # 2 calls return(conn, addr) + 1 KeyboardInterrupt
            assert ClientMock.call_count == 2
            ClientMock.call_args('conn2', 'addr2')                    # args of last call
            assert client_mock_for_start.start.call_count == 2

            # and check server.stop()
            self.assertTrue(socket_mock.close.called)
            self.assertFalse(self.server._running)


if __name__ == '__main__':
    unittest.main()
