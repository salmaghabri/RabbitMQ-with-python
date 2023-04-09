from tkinter import *
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='user2')
def on_text_changed1(event):
    text = event.widget.get("1.0", "end-1c")
    channel.basic_publish(exchange='',
                        routing_key='user2',
                        body=text)
    print( text)



master = Tk("user 2")
Label(master, text='First user').grid(row=0)
Label(master, text='Second user').grid(row=1)
e1 = Text(master, height=10,width=50)
e2 = Text(master, height=10,width=50)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e2.bind("<KeyPress>", on_text_changed1)
e1.config(state='disabled')

mainloop()
   