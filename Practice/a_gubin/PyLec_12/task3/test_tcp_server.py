import unittest
from unittest import mock
from tcp_server import TcpServer
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


class TestTcpServer(unittest.TestCase):

    def test_server(self):

        af_inet = AF_INET
        sock_stream = SOCK_STREAM
        sol_socket = SOL_SOCKET
        so_reuseaddr = SO_REUSEADDR

        with mock.patch("tcp_server.socket") as mock_socket, \
                mock.patch("tcp_server.ClientThread", spec=True) as mock_ClientThread:

            host = 'localhost'
            port = 5555

            tcp_server = TcpServer(host=host, port=port)

            self.assertEqual(tcp_server.host, host)
            self.assertEqual(tcp_server.port, port)
            self.assertIsNone(tcp_server._socket)
            self.assertFalse(tcp_server._runnning)

            def accept_stub():
                ca = [("conn1", "addr1"), ("conn2", "addr2"), ("conn3", "addr3")]
                for i in range(len(ca)):
                    if i == 2:
                        tcp_server.stop()
                    yield ca[i]

            s_socket = mock.Mock(name="s_sock")
            s_socket.accept.side_effect = accept_stub()

            mock_socket.socket.return_value = s_socket
            mock_socket.AF_INET = af_inet
            mock_socket.SOCK_STREAM = sock_stream
            mock_socket.SOL_SOCKET = sol_socket
            mock_socket.SO_REUSEADDR = so_reuseaddr

            tcp_server.run()

            mock_socket.socket.assert_called_once_with(af_inet, sock_stream)
            tcp_server._socket.setsockopt.assert_called_once_with(sol_socket, so_reuseaddr, 1)
            tcp_server._socket.bind.assert_called_once_with((host, port))
            tcp_server._socket.listen.assert_called_once_with(5)
            self.assertFalse(tcp_server._runnning)
            self.assertEqual(tcp_server._socket.accept.call_count, 3)
            self.assertEqual(mock_ClientThread.call_count, 3)
            inst_client_thread = mock_ClientThread("stub", "stub")
            self.assertEqual(inst_client_thread.start.call_count, 3)
            tcp_server._socket.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
