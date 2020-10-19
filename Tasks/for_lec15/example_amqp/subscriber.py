# файл receive.py

import pika
import time
import random

NAME = 'Logger ' + str(random.randint(1, 1000))

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
queue_name = 'hello_1'
result = channel.queue_declare(queue=queue_name, exclusive=True)
channel.queue_bind(exchange='logs', queue=queue_name)


def callback(ch, method, properties, body):
    print(f'Processing msg by {body.decode()}: {NAME}')
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
