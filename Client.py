"""
Script Name : Client.py
Version     : 1.0.0
Description : Client program for TCP/IP socket program
Compatible  : 2.7x
"""

__author__ = 'Amahapa'

# General Imports
import socket
# Local Imports
from Encode_Decode import encode_, decode_

# Global Variables
host = '127.0.0.1'
port = 5000


def Main():
    """
    Function Name : Main
    Parameters    : none
    Return Value  : none
    Purpose       : To act as client code for sending/receiving messages to/from server
    Description   : Simple client socket program that creates a socket object
                    connects to the client using the given host ip address and port.
                    The client sends a encoded message and decodes it using default
                    python encoder and decoder as well as a local encoder for 2 levels of
                    security.
    """
    my_socket = socket.socket()                                                 # Creating the socket object
    my_socket.connect((host, port))                                             # Conecting the host and port to the socket

    print('Welcome to client, type to send a message.')
    print('To quit, type %quit')

    while 1:
        message = raw_input(">>> ")
        if message.lower() == '%quit':                                          # This is to break the while 1 loop
            break

        message = encode_(message)
        my_socket.send(message.encode())                                        # 2nd level encoding using python's default encoding
        data = my_socket.recv(1024).decode()                                    # Sending the data in a 1024 byte stream

        print ('Received from server: ' + data)

        ques = raw_input('Do you wish to decode ? (y/n): ')

        if ques.lower() == 'y':                                                 # To decode the message encoded by local encoder
            print ('decoded message: '+decode_(data.lower()))
        else:
            pass


    print('Connection terminated.')
    my_socket.close()                                                           # Closes the connection


if __name__ == '__main__':
    Main()
