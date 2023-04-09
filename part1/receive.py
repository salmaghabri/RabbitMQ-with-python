import pika, threading
from tkinter import *

def consume(queue):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        label=label1
        if queue=='user2' : 
            label=label2
        label2.after(0, label.config(text=body.decode()))
        
    channel.basic_consume(queue=queue,
                        auto_ack=True,
                        on_message_callback=callback)
    channel.start_consuming()

        


def start_consumer_thread():
    consumer_thread1 = threading.Thread(target=consume,args=("user1",))
    consumer_thread2 = threading.Thread(target=consume,args=("user2",))
    consumer_thread1.start()
    consumer_thread2.start()


root = Tk()
Label(root, text='User 1').grid(row=0)
Label(root, text='User 2').grid(row=1)
label1 = Label(root,height=10,width=50)
label1.grid(row=0, column=1)
label2 = Label(root,height=10,width=50)
label2.grid(row=1, column=1)
start_consumer_thread()
root.mainloop()

# if __name__ == '__main__':
#     try:
#         main()
#         # root.mainloop()
#         # root.mainloop() houni as if fammech gui


#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)