"""
Script Name : Server.py
Version     : 1.0.0
Description : Server program for TCP/IP socket program
Compatible  : 2.7x
"""

__author__ = 'Amahapa'

# General Imports
import socket

# Global Variables
host = "127.0.0.1"
port = 5000


def Main():
    """
    Function Name : Main
    Parameters    : none
    Return Value  : none
    Purpose       : To act as client code for sending/receiving messages to/from server
    Description   : Simple server socket program that creates a socket object
                    connects to the client using the given host ip address and port.
    """
    mySocket = socket.socket()                                                  # Creating the socket object
    mySocket.bind((host, port))                                                 # Conecting the host and port to the socket

    print('Welcome to the server')
    print('Waiting for a connection.....')
    mySocket.listen(1)                                                          # Will only accept one client to connect
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()                                         # Receiving the data in a 1024 byte stream and decoding it
        if not data:                                                            # Terminating the connection if no data is received
            break
        print ("from connected  user: " + str(data))

        data = str(data)
        print ("sending: " + str(data))
        conn.send(data.encode())                                                # Sends the data back to Client after again encoding using python encoder

    print ('connection from: '+str(addr)+' is terminated.')
    conn.close()                                                                # Closes the Connection


if __name__ == '__main__':
    Main()
