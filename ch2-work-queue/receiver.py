import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(channel, method, properties, body):
  print(" [x] Received %r" % body)
  time.sleep(body.count('.'))
  print(" [x] Done")
  channel.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello')

# channel.basic_consume(callback,
                      # queue='hello',
                      # no_ack=True)

print('Reciever is waiting for messages. To exit press CTRL+C')
channel.start_consuming()