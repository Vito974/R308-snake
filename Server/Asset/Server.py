#<--PANCHOO-Ashvin--PATEL-Ibrahim--DAMDJI-Imran-->

import json
import socket
import pickle
import time
import select
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
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
    serpent = Serpent() #Création du serpent
    pomme = Pomme(serpent) #Création de la pomme
    
    position = pomme.set_position() #On place la pomme
    p_position = json.dumps(position) #Sérialisation des données pour l'envoie
    
    clientConnected.send(p_position.encode()) #Envoie des données
    
    time.sleep(2)
    
    s_direction = "U" #Positionnement d'une direction par defaut
    req = 0
    while True :
        ready = select.select([clientConnected], [], [], 1) #Permet de rendre recv non bloquante
        if ready[0]:
            req = clientConnected.recv(4096).decode() #Lecture de la touche appuyé par le client
            print(req)
        
        if(req== "D"): 
            s_direction = "U"
            if(serpent.move("U",position)=="touché"): #On verifie si on atouché la pomme
                position = pomme.set_position() #On replace la pomme
                p_position = json.dumps(position) 
                clientConnected.send(p_position.encode()) #On envoie la nouvelle position de la pomme au serveur
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())

        
        elif(req== "U") :
            s_direction = "D"
            if(serpent.move("D",position)=="touché"):
                position = pomme.set_position()
                p_position = json.dumps(position)
                clientConnected.send(p_position.encode())
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())

        
        elif(req== "L") :
            s_direction = "L"
            if(serpent.move("L",position)=="touché"):
                position = pomme.set_position()
                p_position = json.dumps(position)
                clientConnected.send(p_position.encode())
            serpent.move("L",position)
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())


        elif(req== "R") :
            s_direction = "R"
            if(serpent.move("R",position)=="touché"):
                position = pomme.set_position()
                p_position = json.dumps(position)
                clientConnected.send(p_position.encode())
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())

        else :
            if(serpent.move(s_direction,position)=="touché"):
                position = pomme.set_position()
                p_position = json.dumps(position)
                clientConnected.send(p_position.encode())
            s_position = json.dumps(serpent.get_position())
            clientConnected.send(s_position.encode())
        time.sleep(0.2)
        
