from tkinter import *
class Editor :
    __instance = None
    n=0

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
   
    def add_user(self,channel):
        self.n+=1
        print(f'user {self.n} enetred')
   

    def render(self):
        root = Tk()
        e1 = Text(root, height=10,width=50)
        e2 = Text(root, height=10,width=50)
        # e3 = Text(root, height=10,width=50)
        Label(root, text=' no user').grid(row=0)
        Label(root, text=' no user').grid(row =1)
        # Label(root, text=' no user').grid(row =2)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        # e2.bind("<KeyPress>", on_text_changed1)

        # e3.grid(row=2, column=1)
        

        mainloop()

e=Editor()
e.render()


