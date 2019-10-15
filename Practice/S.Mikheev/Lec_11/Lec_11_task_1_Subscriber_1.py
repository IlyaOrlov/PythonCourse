import pika


NAME = 'even numbers'
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs2', exchange_type='direct')
result = channel.queue_declare(queue='task_queue', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs2', queue=queue_name, routing_key='task_queue')


def callback(ch, method, properties, body, filename='even_numbers.txt'):
    body = body.decode()
    print('Number {} is {}'.format(body, NAME))
    with open(filename, "a") as file:
        file.write('{}, '.format(body))
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
