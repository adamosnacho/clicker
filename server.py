import socket
quitMsg = 'quit'
host = '192.168.0.163'
port = 5000  # initiate port no above 1024
myip = socket.gethostbyname(host)
server = socket.socket()
server.bind((host, port))
print(myip)
connected = False
done = False
server.listen(1)  # accept new connection
while not done:
    if connected == False:
        conn, address = server.accept()
        connected = True
    else:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        conn.send('resp'.encode())
        print(data)
    
        
conn.close()
