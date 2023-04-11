import tkinter as tk
from TextZone import TextZone
from User import User 

class GUI:
    def __init__(self,text_zones,users):
        self.window = tk.Tk()
        self.text_zones = text_zones
        self.text_boxes = {}
        self.users=users
        self.create_widgets()

    def create_widgets(self):
        self.window.title("Text Editor")
        # print("fffffffffffff")
        # Create a label for each text zone
        for text_zone in self.text_zones:
            label_text=f"Text Zone {text_zone.id}"
            if text_zone.user is not None :
                label_text=f'{text_zone.user.username} is writing '


            label = tk.Label(self.window, text=label_text)
            label.grid(column=text_zone.id, row=0)

            # Create a text box for each text zone
            text_box = tk.Text(self.window, height=20, width=40)
            text_box.grid(column=text_zone.id, row=1)
            key=f'queue {text_zone.id}'
            self.text_boxes[key]=text_box

            # text_box.insert('1.0',text_zone.text)
            text_box.bind('<Key>', lambda event, text_zone=text_zone, text_box=text_box: self.on_text_changed(event, text_zone))
            # Disable the text box if the zone is assigned to a user
            # if text_zone.user is not None:
            #     text=text_box.get("1.0", "end-1c")
            #     # text_box.config(state=tk.DISABLED)
            #     print(text)
            #     # text_box.after(0, label.config(text=text))


            # else:
            #     text_box.config(state=tk.NORMAL)
          
            #     text_box.bind('<KeyPress>', lambda event, text_zone=text_zone, text_box=text_box: self.on_text_changed(event, text_zone))
        # self.update_widgets()
    
    def update_widgets(self): 
        for text_zone in self.text_zones:
            text_box=self.text_boxes[f'queue {text_zone.id}']
            # text_zone.producer.start_consuming_threads()
            # text_zone.update_text(text_zone)
            # print('text updated: ',text_zone.text )
            # text_box.after(0,text_box.insert(tk.END,text_zone.text))
            # #text_box.get("1.0", "end-1c")

            




    def add_text_zone(self, text_zone):
        self.text_zones.append(text_zone)



    def on_text_changed(self,event,text_zone):
        text_box=event.widget
        text = text_box.get("1.0", "end-1c")
        text_zone.producer.publish_message(text,text_zone.get_queue_name() )


    def send_message(self, event, text_zone, text_box):
        message = text_box.get("1.0", "end-1c")

        # Send the message to the text zone's RabbitMQ producer
        text_zone.producer.send_message(message)

        # Clear the text box
        text_box.delete("1.0", tk.END)

        # Disable the text box and assign the text zone to the current user
        text_box.config(state=tk.DISABLED)
        text_zone.user = text_zone.get_current_user()


    
    def start(self):
        self.window.mainloop()
   



   
