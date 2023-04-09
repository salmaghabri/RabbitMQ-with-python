from editor import Editor
import pika

# e=Editor()
# e.add_user()
# ee=Editor()
# ee.add_user()
# print(e.n, ee.n)
class user :
    def __init__(self,name,channel) -> None:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        # channel.queue_declare(queue='user')
        self.name=name
        

        



