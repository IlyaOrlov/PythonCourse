import cmd_manager
import mock
import unittest


class TestCmdManager(unittest.TestCase):

    def test_cmd_manager(self):
        cmd_mgr = cmd_manager.CmdManager()

        # Мы тестируем класс CmdManager, объект audit_service нас интересует
        # постольку, поскольку к нему идут обращения от методов CmdManager.
        # Эти обращения можно рассматривать как выходные данные тестируемого
        # класса CmdManager.
        with mock.patch('cmd_manager.audit_service') as audit_service_mock:
            # Метод set_service объекта класса CmdManager принимает
            # в качестве параметра объект service, о котором мы знаем только
            # то, что у него есть атрибут name и метод run, который должен
            # что-то возвращать. Подставим вместо service mock-объект.
            service = mock.Mock()
            service.name = 'MyService'
            service.run.return_value = 0

            cmd_mgr.set_service(service)
            self.assertTrue(service.start.called)

            cmd_mgr.run_command('status')
            # Используем assert-методы mock-объекта, которым мы подменили
            # audit_service
            audit_service_mock.add_call.assert_called_once_with(
                'MyService', 'run', 'status')
            service.run.assert_called_once_with('status')
            audit_service_mock.add_result.assert_called_once_with(
                'MyService', 'run', 0)


if __name__ == '__main__':
    unittest.main()
