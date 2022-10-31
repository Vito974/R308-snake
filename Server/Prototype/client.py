#----- A simple TCP client program in Python using send() function -----

import socket
import json
import pickle
 
# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server
clientSocket.connect(("127.0.0.1",8080));

z = json.dumps([[0,4],[0,5]])


clientSocket.send(z.encode())

# Receive data from server
dataFromServer = clientSocket.recv(4096);

# Print to the console
print(dataFromServer.decode());
