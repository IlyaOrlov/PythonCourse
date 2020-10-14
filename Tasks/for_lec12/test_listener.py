import mock

# Тестируемый класс
class Listener:
    def __init__(self):
        self.running = True

    def listen_forever(self):
        while self.running:
            try:
                msg = msg_broker.wait_message()
                client.process_message(msg)
            except Exception:
                self.running = False

# Подготовка к тестированию
# Создаем объект тестируемого класса
listener = Listener()
# Заменяем зависимости на mock-объекты
msg_broker = mock.Mock()
client = mock.Mock()
# Настраиваем поведение mock-объектов
# При инициализации атрибута side_effect итерируемым объектом
# при каждом обращении к wait_message будет возвращаться очередной
# элемент итерируемого объекта.
msg_broker.wait_message.side_effect = ['message', Exception]

def check_msg(msg):
    assert msg == 'message'
# При инициализации атрибута side_effect функциональным (callable)
# объектом при каждом обращении к process_message будет вызываться
# этот функциональный объект.
client.process_message.side_effect = check_msg

# Тестируем и выполняем проверки
listener.listen_forever()
assert listener.running == False
client.process_message.assert_called_once_with('message')
assert msg_broker.wait_message.call_count == 2