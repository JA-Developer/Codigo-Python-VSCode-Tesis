from ast import While
from multiprocessing import connection
import socket
import sys
import numpy as np

class ControllerClient:

    buffer = ""

    def __init__(self, address, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.server_address = (address, port)
        self.sock.connect(self.server_address)
        #self.sock.settimeout(0.01)

    def sendString(self, Text):
        Data = bytes(str(Text) + ";", 'utf-8')
        self.sock.sendall(Data)

    def getString(self):

        first_value = self.buffer.find(';')

        while (first_value < 0):
            data = self.sock.recv(64)
            if(len(data) > 0):
                self.buffer += data.decode('UTF-8')
                first_value = self.buffer.find(';')
            else:
                return ''
        
        if(first_value >= 0):
            text = self.buffer[:first_value]
            self.buffer = self.buffer[first_value + 1:]
            return text
        else:
            return ''

    def closeConnection(self, N_Connection):
        self.sock.close()