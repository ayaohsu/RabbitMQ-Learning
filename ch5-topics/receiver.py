import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', 
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

topics = sys.argv[1:]
if not topics:
    sys.stderr.write("Usage: %s [topics]...\n" % sys.argv[0])
    sys.exit(1)

for topic in topics:
    channel.queue_bind(exchange='topic_exchange', 
                       queue=queue_name,
                       routing_key=topic)
    print(' Binding %r to queue %r' % (topic, queue_name))

print('\n [*] Waiting for logs for %r. To exit press CTRL+C' % topics)

def callback(channel, method, properties, body):
  print(" [x] Receiving %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print('Reciever is waiting for messages. To exit press CTRL+C')
channel.start_consuming()