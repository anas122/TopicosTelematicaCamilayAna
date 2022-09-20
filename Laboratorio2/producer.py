import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('3.220.79.140', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

print("Runnning Producer Application...")


for i in range(10):
    a=(random.uniform(6,32))
    a=round(a, 2)
    print (a)
    channel.basic_publish(exchange='my_exchange', routing_key='test', body=str(a))
    

print(" [x] Sent 'Hello World...!'")

connection.close()