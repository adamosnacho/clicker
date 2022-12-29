import socket
from getch import getche, getch
host = '192.168.0.163'
port = 5000  # socket server port number
def client_program():
    client_socket = socket.socket()  # instantiate  # connect to the server
    client_socket.connect((host, port))

    done = True
    while done:
        data = client_socket.recv(1024).decode()

        if data !='resp':
            print(data)
        
    client_socket.close()

client_program()