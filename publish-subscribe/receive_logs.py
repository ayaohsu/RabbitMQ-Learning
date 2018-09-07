import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', 
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

print(' Binding exchange to queue %r' % queue_name)
channel.queue_bind(exchange='logs', 
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(channel, method, properties, body):
  print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print('Reciever is waiting for messages. To exit press CTRL+C')
channel.start_consuming()