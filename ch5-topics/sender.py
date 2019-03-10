import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_exchange', 
                         exchange_type='topic')

topic = sys.argv[1] if len(sys.argv) >= 2 else "anonymous.info"

message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange='topic_exchange',
                      routing_key=topic,
                      body=message)

print(" [x] sent %r:%r" % (topic, message))
connection.close()