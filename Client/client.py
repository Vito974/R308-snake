#----- A simple TCP client program in Python using send() function -----

import socket
import json
import pickle
 
# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server
clientSocket.connect(("127.0.0.1",8080));

y=bytes([1,2,2])
clientSocket.send(y)

# Receive data from server
dataFromServer = clientSocket.recv(1024);

# Print to the console
print(dataFromServer.decode());