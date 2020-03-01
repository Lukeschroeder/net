import time
import random
import socket as mysoc


class Server:
    def __init__(self, port):
        self.port = port
        self.socket = self.createsocket()
        self.activesocket = None

    # Returns an active server socket 
    def createsocket(self):
        try:
            serversocket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            print "[S]: Server socket created"
        except mysoc.error as err:
            print '{} \n'.format("socket open error ",err)
        port = self.port
        print('PORT: ', port)
        host = mysoc.gethostname()
        server_binding=(host,port)
        serversocket.bind(server_binding)
        serversocket.listen(1)
        print("[S]: Server host name is: ",host)
        localhost_ip=(mysoc.gethostbyname(host))
        print("[S]: Server IP address is  ",localhost_ip)
        return serversocket

    def accept(self):
        self.activesocket, addr = self.socket.accept()
        print ("[S]: Got a connection request from a client at ", addr)



class Client:
    def __init__(self):
        self.socket = self.createsocket()

    # Returns active client socket
    def createsocket(self):
        # Open client socket
        try:
            clientsocket = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            print "[C]: Client socket created" 
        except mysoc.error as err:
            print '{} \n'.format("socket open error ",err)

        # Return active socket
        return clientsocket

    def connecttoserver(self, hostname, port):
         # Connect to the server at the port passed
        server_binding = (hostname, port)
        self.socket.connect(server_binding)

    


'''
# Continues until client closes socket
while(True):

    # Receive message from client
    data = active_socket.recv(datalength)
    if len(data) == 0: break

    # Convert message to ascii
    converted_data = ''
    for c in data:
        converted_data += str(c)
        converted_data += '_'
    converted_data = converted_data[:-1]

    # Send converted message to client
    active_socket.send(converted_data.encode('utf-8'))


# Close the server socket
server_socket.close()

exit()'''