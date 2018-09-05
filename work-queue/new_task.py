import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

print("Sender created a channel on a localhost connection")

channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print("sender sent '%r'" % message)

connection.close()