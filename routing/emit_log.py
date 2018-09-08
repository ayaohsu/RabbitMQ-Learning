import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

print("Sender created a channel on a localhost connection")

channel.exchange_declare(exchange='direct_logs', 
                         exchange_type='direct')

severity = sys.argv[1]
message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] sent %r:%r" % (severity, message))
connection.close()