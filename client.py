'''client.py: Handles the internal function of the client UI'''
from socket import socket, AF_INET, SOCK_STREAM
from Tkinter import END, DISABLED, NORMAL
class Client(object):
    """Class for Client, handles internally the messages and UI function"""

    def __init__(self, text_area, host='localhost', port=9999):
        """Contructor for Client Class, defines socket connections and receives a
           text area reference from the UI"""
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.area = text_area

    def send_message(self, message):
        """Send the message from the UI to the server via socket defined in constructor"""
        self.client_socket.send(message)

    def message_received(self):
        """Handles the data received via socke and manipulates the area reference from UI
            to show the text in the component"""
        while True:
            data = self.client_socket.recv(1024)
            if data:
                self.area.configure(state=NORMAL)
                self.area.insert(END, str(data))
                self.area.configure(state=DISABLED)
