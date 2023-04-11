import pika
import threading

class Consumer:
    def __init__(self, gui):
        self.text_zones = gui.text_zones
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()   
        self.gui=gui     
        self.exchange=self.channel.exchange_declare(exchange='to_text_zones', exchange_type='fanout')
        # Create a unique queue for the consumer to listen to
        result = self.channel.queue_declare('gui_queue')
        
        # Bind the queue to all the text zones using their routing keys
        for text_zone in self.text_zones:
            self.channel.queue_bind(exchange='to_text_zones', queue='gui_queue', routing_key=text_zone.get_queue_name())
        
        #declare queues to listen to 
        for text_zone in self.text_zones:
            self.channel.queue_declare(queue=text_zone.get_queue_name(),exclusive=False)



    def consume(self,text_zone):
        if text_zone.user :
            print(text_zone.get_queue_name())
            self.channel.basic_consume(queue=text_zone.get_queue_name(), on_message_callback=self.on_message, auto_ack=True)
            self.channel.start_consuming()

    
    def on_message(self, channel, method, properties, body):
        routing_key = method.routing_key
        print(f'consumed message : {body} from {routing_key }')
        self.channel.basic_publish(exchange='to_text_zones', routing_key='', body=body)
        text_box=self.gui.text_boxes[routing_key]

        

    def start_consuming_threads(self):
        for text_zone in self.text_zones:
            self.consuming_thread = threading.Thread(target=self.consume,args=(text_zone,))
            self.consuming_thread.start()

    # def stop_consuming_thread(self):
    #     self.channel.stop_consuming()
    #     self.consuming_thread.join()

    def disconnect(self,text_zone):
        self.channel.close()
        self.connection.close()
