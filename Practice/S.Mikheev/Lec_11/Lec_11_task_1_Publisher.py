import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs2', exchange_type='direct')
channel.confirm_delivery()  # Переводим в режим подтверждения и брокер должен вернуть его,
                            # может не работает в режиме обменника?
Keys = ['task_queue', 'task_queue1']

for i in range(1, 100):
    if i % 2 == 0:
        key = Keys[0]
    else:
        key = Keys[1]
    was_delivered = channel.basic_publish(
        exchange='logs2',
        routing_key=key,
        body=('{}'.format(i)).encode(),
        properties=pika.BasicProperties(
            content_type='text/plain',
            delivery_mode=2))  # Почему то не могу установить флаг mandatory=True... Нужен ли он для подтверждения?
    if was_delivered:  # У меня не получилось получить подтверждение доставки, был бы рад подсказке...
        print('Message {}  has been delivered to queue {}'.format(i, key))
    else:
        print('ERROR: message {} could not be sent!'.format(i))  # В итоге подтверждения не получаю
    time.sleep(1)
connection.close()
