import json
import socket
import pickle
<<<<<<< HEAD
import time
from Classe import *
# Create a stream based socket(i.e, a TCP socket)
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Bind and listen
serverSocket.bind(("",8080));
serverSocket.listen();
# Accept connections

while(True):
    (clientConnected, clientAddress) = serverSocket.accept();
    serverSocket.settimeout(3)
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    serpent = Serpent()
    pomme = Pomme(serpent)
    position = json.dumps(pomme.set_position())
    req = clientConnected.recv(4096).decode()
    clientConnected.send(position.encode())
    time.sleep(4)
    s_direction = "U"
    req = 0
    while True :
        print("je recommence")
        if(req== "U"):
            s_direction = "U"
            serpent.move("U",position)
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())

        
        elif(req== "D") :
            s_direction = "D"
            serpent.move("D",position)
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())

        
        elif(req== "L") :
            s_direction = "L"
            serpent.move("L",position)
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())


        elif(req== "R") :
            s_direction = "R"
            serpent.move("R",position)
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())

        else :
            serpent.move(s_direction,position)
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())
        time.sleep(1)
        


    #dataFromClient = clientConnected.recv(4096).decode()
    #dataFromClient = json.loads(dataFromClient)
    #print(dataFromClient);
    
    # Send some data back to the client
    #clientConnected.send("Hello Client!".encode());
    #z = json.dumps([4,5])
    #y = json.dumps([10,10])
    #clientConnected.send(z.encode())
    #time.sleep(2.5)
    #clientConnected.send(y.encode())
    #time.sleep(2.5)
    #dataFromClient = clientConnected.recv(4096).decode()
    #print(dataFromClient);





    #dataFromClient = clientConnected.recv(4096).decode()
    #print(dataFromClient)
=======

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
>>>>>>> f14a65b9eacc15bee7c4437deeead8ddcdee78dd
