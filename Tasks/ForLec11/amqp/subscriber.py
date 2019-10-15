# файл receive.py

import pika
import time
import random

NAME = 'Logger ' + str(random.randint(1, 1000))

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    print('Processing msg by {}: {}'.format(body.decode(), NAME))
    channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()