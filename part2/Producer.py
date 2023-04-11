import threading
import tkinter as tk
import pika
class Producer :
    exchange=None
    def __init__(self):
        self.msg=''
        self.connection_produce = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_produce = self.connection_produce.channel()
        

        self.connection_consume = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_consume = self.connection_consume.channel()
        self.result=self.channel_produce.queue_declare(queue='listen')
        self.channel_consume.queue_bind(exchange='to_text_zones', queue='listen')



    #declare queues to send messages to
    def declare_queue_produce(self, queue_name):
        self.channel_produce.queue_declare(queue=queue_name)
        
        
    def publish_message(self, message, routing_key):
        self.channel_produce.basic_publish(exchange='', routing_key=routing_key, body=message)
        print("first publish ", message)


#get messages of updates from all the textzones
    def on_message(self,ch, method, properties, body):
            self.msg=body
            # text_zone.after(0,text_zone.insert(tk.END,body))
            print('second  consume',body )

    
    
    
    def close_connection(self): 
        self.connection.close()
    

    def consume(self):
        self.channel_produce.basic_consume(queue='listen', on_message_callback=self.on_message, auto_ack=True)
        print('Waiting for messages...')
        self.channel_produce.start_consuming()

    
    # def on_message(self, channel, method, properties, body):
    #     routing_key = method.routing_key
    #     print(f'consumed message : {body} from {routing_key }')
    #     self.channel_produce.basic_publish(exchange='to_text_zones', routing_key=routing_key, body=body)

        

    def start_consuming_threads(self):
        self.consuming_thread = threading.Thread(target=self.consume)
        self.consuming_thread.start()


    