import threading
import tkinter as tk
import pika
class Producer :
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.result=self.channel.queue_declare(queue='listen')
        self.channel.queue_bind(exchange='to_text_zones', queue='listen')
        self.msg=''
        self.start_consuming_threads()



    #declare queues to send messages to
    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)


    def publish_message(self, message, routing_key):
        print(message, 'in producer')
        self.channel.basic_publish(exchange='', routing_key=routing_key, body=message)




#get messages of updates from all the textzones
    def on_message(self,ch, method, properties, body):
            self.msg=body
            # text_zone.after(0,text_zone.insert(tk.END,body))
            print("Received message f wost l producer:", self.msg)
    
    
    
    def close_connection(self): 
        self.connection.close()
    

    def consume(self):
        self.channel.basic_consume(queue='listen', on_message_callback=self.on_message, auto_ack=True)
        print('Waiting for messages...')
        self.channel.start_consuming()

    
    # def on_message(self, channel, method, properties, body):
    #     routing_key = method.routing_key
    #     print(f'consumed message : {body} from {routing_key }')
    #     self.channel.basic_publish(exchange='to_text_zones', routing_key=routing_key, body=body)

        

    def start_consuming_threads(self):
        self.consuming_thread = threading.Thread(target=self.consume)
        self.consuming_thread.start()


    