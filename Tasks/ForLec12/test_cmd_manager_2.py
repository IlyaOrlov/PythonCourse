import cmd_manager
import mock
import unittest


class TestCmdManager(unittest.TestCase):

    @mock.patch('cmd_manager.audit_service')
    def test_cmd_manager(self, audit_service_mock):
        cmd_mgr = cmd_manager.CmdManager()
        service = mock.Mock()
        service.name = 'MyService'
        service.run.return_value = 0
        cmd_mgr.set_service(service)
        self.assertTrue(service.start.called)
        cmd_mgr.run_command('status')
        # Используем assert-методы mock-объекта, которым мы подменили
        # audit_service
        audit_service_mock.add_call.assert_called_once_with('MyService',
                                                            'run', 'status')
        service.run.assert_called_once_with('status')
        audit_service_mock.add_result.assert_called_once_with('MyService',
                                                              'run', 0)


if __name__ == '__main__':
    unittest.main()
