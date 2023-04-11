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
    consumer=Consumer()

    p1=Producer()
    p2=Producer()
    p3=Producer()
    p4=Producer()
    t1 = TextZone(1)
    t2 = TextZone(2)
    t3 = TextZone(3)
    t4 = TextZone(4)
    t1.add_producer(p1)
    t2.add_producer(p2)
    t3.add_producer(p3)
    t4.add_producer(p4)
    user=User('user1')

    # t3.assign_user(user)
    t2.assign_user(user)
    gui = GUI([t1,t2,t3],[user])



    def worker(gui):
        gui.window.after(0, gui.create_widgets)


    render_thread = threading.Thread(target=worker, args=(gui,))
    # render_thread.start()
    # gui.add_text_zone()

    consumer.add_gui(gui)
    consumer.start_consuming_threads()
    gui.start()

