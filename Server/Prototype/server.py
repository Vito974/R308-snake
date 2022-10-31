#----- A simple TCP based server program in Python using send() function -----

 
import json
import socket
import pickle

# Create a stream based socket(i.e, a TCP socket)
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Bind and listen
serverSocket.bind(("",8080));
serverSocket.listen();

# Accept connections
while(True):
    (clientConnected, clientAddress) = serverSocket.accept();
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    
    dataFromClient = clientConnected.recv(4096).decode()
    dataFromClient = json.loads(dataFromClient)
    print(dataFromClient);
    
    # Send some data back to the client
    clientConnected.send("Hello Client!".encode());
    