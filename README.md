## RabbitMQ-Learning
This is the repo for RabbitMQ Tutorial and Sandbox code

## Introduction
__Message Queue__: used for __inter-process communication__, or __inter-thread communication__ within the same process

__Message Broker__: an intermediary program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver. It is for the purpose of decoupling.

__Message protocals__: AMQP(RabbitMQ implements this), MQTT, STOMP, etc. These are __application layer__ protocals.

![alt text](https://github.com/ayaohsu/RabbitMQ-Learning/blob/master/bin/AMQP-diagram.png)

Advanced Message Queuing Protocol

RabbitMQ is coded in Erland language to implement the AMQP protocal

### Architecture
![alt text](https://github.com/ayaohsu/RabbitMQ-Learning/blob/master/bin/AMQP-architecture.jpg)
- One single TCP connection
- Channel on the server side to multicast; de-multicast on the client side

### 'Hello World'
Terms:
- A producer is a user application that sends messages
- A queue is a buffer that stores messages
- A consumer is a user application that receives messages

In RabbitMQ, a message can never be sent directly to the queue, it always needs to go through an exchange.
Exchange: Exchanges take a message and route it into zero or more queues

Queue: 
- Name
- Durability
- Bindings
  - Bindings are rules that exchanges use to route messages to queues

### Work Queue
- The main idea behind Work Queues (aka: Task Queues) is to avoid doing a resource-intensive task immediately and having to wait for it to complete
- We encapsulate a task as a message and send it to the queue
- RabbitMQ uses round-robin to distribute the messages to the consumers
- __Ack(nowledgment)__: consumer sends back an ack to RabbitMQ, to indicate that the message has been received and processed and that RabbitMQ is free to delete it.
- If a consumer dies (connection is lost) without sending an ack, RabbitMQ will re-queue it. It will then quickly redeliver it to another consumer.
- This is to make sure that no message is lost and not processed.

### Publish/Subscribe
exchange type: 
- Direct Exchange:
  - A queue binds to the exchange with a routing key K
  - When a new message with routing key R arrives at the direct exchange, the exchange routes it to the queue if K = R
- Fanout Exchange:
  - Broadcast all the messages it receives to all the queues it knows

Binding: an exchange can __bind__ with a queue

### Topics
Topic Exchange: 
- Messages sent to topic exchange can't have an arbitrary routing_key - it must be a list of words, delimited by dots.
- Binding key: must be in the same format
- Two special chars:
  - '*' can substitute for exactly one word
  - '#' can substitute for zero or more worlds

## Resource
https://www.rabbitmq.com/tutorials/tutorial-one-python.html

## Windows Resouce
- RabbitMQ command line on localhost: 
`rabbitmqctl`
- To list all the queues:
`rabbitmqctl list_queues`
