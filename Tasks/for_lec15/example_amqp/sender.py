import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello', durable=True)

for i in range(5):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=f'Hello World {i}'.encode(),
                          properties=pika.BasicProperties(delivery_mode=2))
print("Sent 'Hello World!'")
connection.close()