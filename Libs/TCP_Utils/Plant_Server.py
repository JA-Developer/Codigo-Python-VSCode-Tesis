from ast import While
from multiprocessing import connection
import socket
import sys


class PlantServer:

    connections = []
    buffer = ""

    def __init__(self, address, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Bind the socket to the port
        server_address = (address, port)
        self.sock.bind(server_address)

    def listen(self):
        # Listen for incoming connections
        self.sock.listen(1)
        connection, client_address = self.sock.accept()
        connection.settimeout(0.01)
        self.connections.append(connection)

    def sendString(self, Text, N_Connection):
        Data = bytes(str(Text) + ";", 'utf-8')
        self.connections[N_Connection].sendall(Data)

    def getString(self, N_Connection):
        try:
            first_value = self.buffer.find(';')

            while (first_value < 0):
                
                data = self.connections[N_Connection].recv(64)
                
                if(len(data) > 0):
                    self.buffer += data.decode('UTF-8')
                    first_value = self.buffer.find(';')
                else:
                    return ''
        except:
            return ''
        
        if(first_value >= 0):
            text = self.buffer[:first_value]
            self.buffer = self.buffer[first_value + 1:]
            return text
        else:
            return ''

    def closeConnection(self, N_Connection):
        self.connections[N_Connection].close()