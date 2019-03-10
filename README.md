## RabbitMQ-Learning
This is the repo for RabbitMQ Tutorial and Sandbox code
__RabbitMQ__ is a message-broker middleware software that implements AMQP protocol.

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
Exchange type: Fanout
  - Broadcast all the messages it receives to all the queues it knows
  - The value of `routing_key` is ignored for a `fanout` exchange to forward a message

### Routing
Exchange Type: Direct
- It routes a message to all the queues whose `binding key` matches the `routing key` of the binding

__Binding__: A binding is a relationship between an exchange and a queue. It can be simply read as: the queue is interested in messages from the exchange

__binding_key__: a property of a binding, which is the relationship between queue and exchange 
__routing_key__: the routing information we provide when sending a message

### Topics
Exchange Type: Topic
- Messages sent to topic exchange can't have an arbitrary routing_key - __it must be a list of words, delimited by dots.__
- Binding key: must be in the same format
- Two special chars for binding key
  - '*' can substitute for exactly one word
  - '#' can substitute for zero or more worlds
- Please note that wild card only applies to binding key, but not routing key

## Resource
https://www.rabbitmq.com/tutorials/tutorial-one-python.html

## Windows Resouce
- RabbitMQ command line on localhost: 
`rabbitmqctl`
- To list all the queues:
`rabbitmqctl list_queues`

### Virtual host
- provides logical groupinp, separation of physical resources and resource permissions
- when an AMQP client connects to RabbitMQ, it specifies a vhost name to connect to
- if the authentication succeeds and the credential provided by the clients was granted, connection is established
