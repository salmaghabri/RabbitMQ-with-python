import pika
import threading

class Consumer:
    def __init__(self):
           
        self.text_zones = []
        self.gui=None
        #consume from text_zones
        self.connection_consume = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        # self.channel_consume=self.connection_consume.channel()


        self.start_consuming_threads()
        #declare queues to listen to 
        for text_zone in self.text_zones:
            channel=self.connection_consume.channel()
            channel.queue_declare(queue=text_zone.get_queue_name(),exclusive=False)
        # Create a unique queue for the consumer to listen to
        

        #broadcast
        self.connection_broadcast = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_broadcast = self.connection_broadcast.channel()   
        result = self.channel_broadcast.queue_declare('gui_queue')
        self.exchange_broadcast=self.channel_broadcast.exchange_declare(exchange='to_text_zones', exchange_type='fanout')
        # Bind the queue to all the text zones using their routing keys
        for text_zone in self.text_zones:
            self.channel_broadcast.queue_bind(exchange='to_text_zones', queue='gui_queue', routing_key=text_zone.get_queue_name())
        


    def add_gui(self, gui): 
        self.text_zones = gui.text_zones
        self.gui=gui  

    def consume(self,text_zone):
        
        if text_zone.user:
            
            print(text_zone.get_queue_name())
            channel_consume=self.connection_consume.channel()
            channel_consume.basic_consume(queue=text_zone.get_queue_name(), on_message_callback=self.on_message, auto_ack=True)
            channel_consume.start_consuming()

    
    def on_message(self, channel, method, properties, body):
        routing_key = method.routing_key
        print(f'first consume {body} from {routing_key }')
        self.channel_broadcast.basic_publish(exchange='to_text_zones', routing_key='', body=body)
        print(f'second produce {body} from {routing_key }')

        text_box=self.gui.text_boxes[routing_key]

        

    def start_consuming_threads(self):
        for text_zone in self.text_zones:
            consuming_thread = threading.Thread(target=self.consume,args=(text_zone,))
            consuming_thread.start()

    # def stop_consuming_thread(self):
    #     self.channel.stop_consuming()
    #     self.consuming_thread.join()

    def disconnect(self,text_zone):
        self.channel.close()
        self.connection.close()
