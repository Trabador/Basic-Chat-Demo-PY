from Tkinter import *
from threading import *
from client import Client

class clientUI():
    """docstring"""

    def __init__(self,root):
        """docstring"""
        root.title("Chat Rule")
        root.minsize(width=400,height=400)

        self.name =  None
        self.message = StringVar()
        frame = Frame(root)
        frame.pack(side=TOP)
        self.create_widgets(frame)

        self.clientInst = Client(self.textArea)
        msg_rev = Thread(target=self.clientInst.message_received)
        msg_rev.daemon = True
        msg_rev.start()
        self.createThreads()


    def create_widgets(self,frame):
        """docstring"""
        self.entryMsg = Entry(frame,width=50,textvariable=self.message)
        self.sendBtn = Button(frame,text="Enviar",relief=RIDGE,command=self.sendBtnAction)

        self.sendBtn.pack(side=BOTTOM)
        self.entryMsg.pack(side=BOTTOM)

        self.textArea = Text(frame,height=26, width=50)
        scrollY = Scrollbar(frame,command=self.textArea.yview)
        self.textArea.configure(yscrollcommand=scrollY.set)
        self.textArea.pack(side=LEFT)

        scrollY.pack(side=RIGHT,fill=Y)

    def createThreads(self):
        pass


    def sendBtnAction(self):
        text = str(self.message.get())+"\n"
        self.clientInst.send_message(text)
        self.message.set("")


if __name__=='__main__':
    root = Tk()
    app = clientUI(root)
    root.mainloop()
