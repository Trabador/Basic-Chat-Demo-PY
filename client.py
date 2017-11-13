from socket import *
from threading import *
from Tkinter import END
import sys

class Client():
    """docstring"""

    def __init__(self,textA,host='localhost',port=9999):
        """docstring"""
        self.clientSocket = socket(AF_INET,SOCK_STREAM)
        self.clientSocket.connect((host,port))
        self.area = textA

    '''def run_client(self):
        msg_rev = Thread(target=self.message_received)
        msg_rev.daemon = True
        msg_rev.start()

        while True:
            msg = raw_input("->")
            self.send_message(msg)'''


    def send_message(self,message):
        """docstring"""
        self.clientSocket.send(message)

    def message_received(self):
        """docstring"""
        while True:
            data = self.clientSocket.recv(1024)
            if data:
                self.area.insert(END,str(data))