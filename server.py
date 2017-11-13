from socket import *
from threading import *
import sys
class Server():
    """docstring here"""

    def __init__(self):
        '''docstring'''
        self.clients =  []
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.bind(('localhost',9999))
        self.serverSocket.listen(5)

    def process_messages(self, con, add):
        '''docstring'''
        while True:
            try:
                data = con.recv(1024)
                print data
                msn = "User "+str(add[1])+":"+data
                for client in self.clients:
                    client.send(msn)
            except:
                self.clients.remove(con)
                break
            '''size = len(self.clients)
            if size > 0:
                for client in self.clients:
                    try:
                        data = client.recv(1024)
                        if data != None:
                            self.send_msg_to_all(data)
                    except:
                        self.clients.remove(client)'''

    def send_msg_to_all(self, data):
        '''docstring'''
        for client in self.clients:
            client.send(data)

    def create_threads(self,c,a):
        '''docstring'''
        clientThread = Thread(target=self.process_messages,args=(c,a))
        clientThread.daemon = True
        clientThread.start()

    def connection_handler(self):
        '''docstring'''
        while True:
            try:
                con, add = self.serverSocket.accept()
                self.clients.append(con)
                print add
                print self.clients
            except:
                pass

    def run_server(self):
        '''docstring'''
        while True:
            con, add = self.serverSocket.accept()
            self.create_threads(con,add)
            self.clients.append(con)
            print(add)
            print self.clients

my_Server = Server()
my_Server.run_server()
