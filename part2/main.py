import threading
import tkinter as tk
import pika
from TextZone import TextZone
from User import User
from GUI import GUI
from Producer import Producer
from Consumer import Consumer
if __name__ == '__main__':
    # Initialize the GUI and text zones
    p1=Producer()
    p2=Producer()
    p3=Producer()
    p4=Producer()
    t1 = TextZone(1,Producer())
    t2 = TextZone(2,p2)
    t3 = TextZone(3,p3)
    t4 = TextZone(4,p4)
    user=User('ena')

    # t1.assign_user(user)
    gui = GUI([t1,t2,t3],[user])
    # gui.text_zones=[t1,t2,t3]

    # consumer_thread = threading.Thread(target=consumer.consume)
    # consumer_thread.start()
    def worker(gui):
        gui.window.after(0, gui.create_widgets)


    render_thread = threading.Thread(target=worker, args=(gui,))
    render_thread.start()
    gui.add_text_zone(TextZone(4,Producer()))
    t1.assign_user(user)
    consumer=Consumer(gui)
    consumer.start_consuming_threads()
    gui.start()

