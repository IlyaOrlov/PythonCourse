import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')

for i in range(5):
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=f'Hello World {i}'.encode())
print("Sent 'Hello World!'")
connection.close()