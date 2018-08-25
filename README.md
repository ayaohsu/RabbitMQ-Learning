## RabbitMQ-Learning
This is the repo for RabbitMQ Tutorial and Sandbox code

## Introduction
Message Queue: used for __inter-process communication__, or __inter-thread communication__ within the same process

Message Broker: an intermediary program module that translates a message from the formal messaging protocol of the sender to the formal messaging protocol of the receiver. It is for the purpose of decoupling.

Message protocals: AMQP(RabbitMQ implements this), MQTT, STOMP, etc. These are __application layer__ protocals.

### 'Hello World'
Terms:
- A producer is a user application that sends messages
- A queue is a buffer that stores messages
- A consumer is a user application that receives messages.

In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
Exchange: Exchanges take a message and route it into zero or more queues

Queue: 
- Name
- Durability
- Bindings
  - Bindings are rules that exchanges use to route messages to queues

Model:
https://www.rabbitmq.com/tutorials/amqp-concepts.html

### Work Queue
The main idea behind Work Queues (aka: Task Queues) is to avoid doing a resource-intensive task immediately and having to wait for it to complete

We encapsulate a task as a message and send it to the queue

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
