import pika
class Producer :
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()


    #declare queues to send messages to
    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)


    def publish_message(self, message, routing_key):
        self.channel.basic_publish(exchange='', routing_key=routing_key, body=message)

    def close_connection(self): 
        self.connection.close()

    