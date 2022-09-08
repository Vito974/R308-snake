import json
import socket
import pickle

# Créer un socket basé sur le flux (c'est-à-dire un socket TCP)
# fonctionnant sur le schéma d'adressage IPv4
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
print("Socket créé...")

# Lier et écouter
serverSocket.bind(("",8080));
serverSocket.listen();
print('Server en ecoute')

# Accepter les connexions
while(True):
    (clientConnected, clientAddress) = serverSocket.accept();
    print("Accepte la demande de connexion de %s:%s"%(clientAddress[0], clientAddress[1]));

    dataFromClient = clientConnected.recv(1024)

    print(list(dataFromClient));

    # Send some data back to the client
    clientConnected.send("Hello Client!".encode());