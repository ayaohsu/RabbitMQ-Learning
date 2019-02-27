import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(channel, method, properties, body):
  print("receiver received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print('Reciever is waiting for messages. To exit press CTRL+C')
channel.start_consuming()