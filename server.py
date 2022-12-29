import socket
quitMsg = 'quit'
host = '192.168.0.163'
port = 5000  # initiate port no above 1024
myip = socket.gethostbyname(host)
server_socket = socket.socket()
server_socket.bind((host, port))
print(myip)
connected = False
done = False
server_socket.listen(1)  # accept new connection
while not done:
    if connected == False:
        conn, address = server_socket.accept()
        connected = True
    else:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()

    print(data)
    
        
conn.close()