class TextZone:
    def __init__(self, id):
        self.id = id
        self.producer = None

        self.user = None
        self.text = ""
        
    def add_producer(self, producer): 
        self.producer=producer
        self.producer.declare_queue_produce(self.get_queue_name())


    def assign_user(self, user):
        if self.user is not None:
            return False
        self.user = user
        # self.producer.declare_queue_produce(self.get_queue_name())
        return True
        
    def get_current_user(self): 
        return self.user 
    
    def get_queue_name(self): 
        return f'queue {self.id}'

    def remove_user(self):
        self.user = None
        
    def update_text(self):
        print('salut')
        self.text=self.producer.msg



