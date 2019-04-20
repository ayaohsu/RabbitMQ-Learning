This is the repo for RabbitMQ Tutorial and Sandbox code

## Introduction
__RabbitMQ__: a message-broker middleware software that implements AMQP protocol (Advanced Message Queuing Protocol, an application layer protocol for message-broker). It is implementedin Erland language.

__Message Queue__: used for __inter-process communication__, or __inter-thread communication__ within the same process

__Message Broker__: an intermediary program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver. It is for the purpose of decoupling.

__Message protocals__: AMQP(RabbitMQ implements this), MQTT, STOMP, etc. These are __application layer__ protocals.

![alt text](https://github.com/ayaohsu/RabbitMQ-Learning/blob/master/bin/AMQP-diagram.png)

### Architecture
__Connection__: A connection is a TCP connection between your application and the RabbitMQ broker

__Channel__: A channel is a virtual connection inside a connection. When you are publishing or consuming messages from a queue - it's all done over a channel
![alt text](https://github.com/ayaohsu/RabbitMQ-Learning/blob/master/bin/AMQP-architecture.jpg)

### 'Hello World'
Terms:
- A __producer__ is a user application that sends messages
- A __queue__ is a buffer that stores messages
- A __consumer__ is a user application that receives messages

In RabbitMQ, a message can never be sent directly to the queue, it always needs to go through an exchange.
__Exchange__: Exchanges take a message and route it into zero or more queues

Durability is a queue's property:
  - Durable queues are persisted to disk and thus survive broker restarts
  - It does not make the messages persistent
```
channel.queue_declare(queue='hello', durable=True)
```

Persistence is the message's property:
  - To mark a message as persistent, set its delivery mode to 2
```
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
```
Message Properties: it's message metadata attributes that can be set when a message is published. Some of the attributes are well-known and mentioned in the AMQP specification. Some examples are:
- Content type
- Persistent
- Time stamp

### Work Queue
- The main idea behind Work Queues (aka: Task Queues) is to avoid doing a resource-intensive task immediately and having to wait for it to complete
- We encapsulate a task as a message and send it to the queue
- RabbitMQ uses round-robin to distribute the messages to the consumers
- __Ack(nowledgment)__: consumer sends back an ack to RabbitMQ, to indicate that the message has been received and processed and that RabbitMQ is free to delete it.
- If a consumer dies (connection is lost) without sending an ack, RabbitMQ will re-queue it. It will then quickly redeliver it to another consumer.
- This is to make sure that no message is lost and not processed.

### Publish/Subscribe
Exchange type: __Fanout__
  - Broadcast all the messages it receives to all the queues it knows
  - The value of `routing_key` is ignored for a `fanout` exchange to forward a message

### Routing
Exchange Type: __Direct__
- It routes a message to all the queues whose `binding key` matches the `routing key` of the binding

__Binding__: A binding is a relationship between an exchange and a queue. It can be simply read as: the queue is interested in messages from the exchange

__binding_key__: a property of a binding, which is the relationship between queue and exchange 
__routing_key__: the routing information we provide when sending a message

### Topics
Exchange Type: __Topic__
- Messages sent to topic exchange can't have an arbitrary routing_key - __it must be a list of words, delimited by dots.__
- Binding key: must be in the same format
- Two special chars for binding key
  - '*' can substitute for exactly one word
  - '#' can substitute for zero or more worlds
- Please note that wild card only applies to binding key, but not routing key

## Resource
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html

### Virtual host
- provides logical groupinp, separation of physical resources and resource permissions
- when an AMQP client connects to RabbitMQ, it specifies a vhost name to connect to
- if the authentication succeeds and the credential provided by the clients was granted, connection is established

### isatm rabbit lib
RabbitMQ consumer pattern
Library code:
1. Have a consumer abstract class. Have a interface to process the messages
2. When creating a queue, pass in the consumer of the queue
3. The queue will keep consuming from the rabbitMQ connection, when it gets a message, it calls the consumer to process the message

Application code:
Construct an application consumer to inherent from the consumer abstract class. Set up connection and channel and queue. Pass the consumer instance to the queue.

_Remaining tasks: understand application rabbitMQ setup, understand rabbitMQ console usage
look at isatmrabbit
vhost note
are we acking messages?
are we persisting the messages?
are we making the queue durable?
what is our naming convention?
are we using exclusive queues?
how many consumers are there for a queue?
how many connections are there for a task?
Draw a rabbit MQ architecture diagram_
