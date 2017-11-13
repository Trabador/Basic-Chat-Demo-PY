from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
class Server(object):
    """Class for the server"""

    def __init__(self):
        '''Constructor for the Server Class. Do not recive paramaters,
           clients is an array for the clients connected to the server'''
        self.clients = []
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('localhost', 9999))
        self.server_socket.listen(5)

    def process_messages(self, con, add):
        '''Process the message received from client socket adding user data.
           If the client is disconnected removes the connection from the list'''
        while True:
            try:
                data = con.recv(1024)
                print data
                msn = "User "+str(add[1])+":"+data
                self.send_msg_to_all(msn)
            except Exception as exception:
                self.clients.remove(con)
                break

    def send_msg_to_all(self, data):
        '''Send the message to all clients in the list ,
           including the original sender'''
        for client in self.clients:
            client.send(data)

    def create_threads(self, con, add):
        '''Creates a thread in daemon mode to handle each connection from each client.
           Receives a connection and adress from client socket'''
        client_thread = Thread(target=self.process_messages, args=(con, add))
        client_thread.daemon = True
        client_thread.start()

    def run_server(self):
        '''Run the main thread in the class. This is the method in charge
           of handling new connections from the clients, creating a thread for each connection
           and adding the new connection to the connections list'''
        while True:
            connection, address = self.server_socket.accept()
            self.create_threads(connection, address)
            self.clients.append(connection)
            print "Clients connected"
            print "=========================================================================>"
            print self.clients

#Instancing the class and running
if __name__ == '__main__':
    SERVER = Server()
    SERVER.run_server()
