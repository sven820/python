__author__ = "JJ.sven"

import pika

''' 客户端连接的时候需要配置认证参数
credentials = pika.PlainCredentials('alex', 'alex3714')


connection = pika.BlockingConnection(pika.ConnectionParameters(
    '10.211.55.5',5672,'/',credentials))
channel = connection.channel()
'''

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()