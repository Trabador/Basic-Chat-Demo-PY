from Tkinter import (Tk, StringVar, Entry, Button, Frame, Text, Scrollbar,
                     BOTTOM, LEFT, RIGHT, TOP, RIDGE, Y)
from threading import Thread
from client import Client

class ClientUI(object):
    """Class for the client User Interface"""

    def __init__(self,root):
        """Contructor for the User Interface Window.
           Receives the root window from Tk inter as parameter"""
        root.title("Chat Demo PY")
        root.minsize(width=400, height=400)

        self.message = StringVar()
        frame = Frame(root)
        frame.pack(side=TOP)
        self.create_widgets(frame)

        self.client_instace = Client(self.messages_area)
        self.create_msg_recv_thread()


    def create_widgets(self, frame):
        """Creates all the visual components inside the window for the client UI"""
        self.entry_message = Entry(frame, width=50, textvariable=self.message)
        self.send_button = Button(frame, text="Enviar", relief=RIDGE,
                                  command=self.send_button_action)

        self.send_button.pack(side=BOTTOM)
        self.entry_message.pack(side=BOTTOM)

        self.messages_area = Text(frame, height=26, width=50)
        vertical_scroll = Scrollbar(frame, command=self.messages_area.yview)
        self.messages_area.configure(yscrollcommand=vertical_scroll.set)
        self.messages_area.pack(side=LEFT)

        vertical_scroll.pack(side=RIGHT, fill=Y)

    def create_msg_recv_thread(self):
        '''Creates the thread in daemon modethat handles the receiving messages from server.
           Uses the instance of Client class to proccess the message to show in it the UI'''
        msg_rev = Thread(target=self.client_instace.message_received)
        msg_rev.daemon = True
        msg_rev.start()


    def send_button_action(self):
        '''Uses the instance of the Client class , gets the text data from the component
           and calls for the function in the instance'''
        text = str(self.message.get())+"\n"
        self.client_instace.send_message(text)
        self.message.set("")

#Create instance of window and application for clint UI
if __name__ == '__main__':
    ROOT = Tk()
    APP = ClientUI(ROOT)
    ROOT.mainloop()
