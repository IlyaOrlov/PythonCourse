import pika


from pika.exceptions import UnroutableError

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs2', exchange_type='direct')
channel.confirm_delivery()
Keys = ['task_queue', 'task_queue1']

for i in range(1, 100):
    if i % 2 == 0:
        key = Keys[0]
    else:
        key = Keys[1]
    try:
        channel.basic_publish(
            exchange='logs2',
            routing_key=key,
            body=('{}'.format(i)).encode(),
            properties=pika.BasicProperties(
                content_type='text/plain',
                delivery_mode=2),
            mandatory=True)
    except UnroutableError:
        print('ERROR: message: \'{}\' could not be sent from queue {}!'.format(i, key))
    else:
        print('Message: \'{}\' has been delivered to queue {}'.format(i, key))
connection.close()
