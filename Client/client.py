#Importation
import pygame
from pygame.locals import *
import pygame, sys
import numpy
import socket
import json
import time

# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server
clientSocket.connect(("127.0.0.1",8080));

# Initialisation
pygame.init()
screen = pygame.display.set_mode((400, 400))
couleurs = numpy.random.randint (0, 255, size = (4,3))
pygame.display.set_caption('Snake Game')
pygame.draw.rect (screen, couleurs[2], (10, 10, 20, 20))

#Personnalisation du background
background = pygame.image.load("image/Bg.png")
#pygame.mouse.set_visible(False)

#fonction d'affichage du Serpent

def affiche_S(S):
    #Initialisation des variables d'affichage
    tête = pygame.image.load('image/t.png')
    têteH = pygame.image.load('image/TH.png')
    têteB = pygame.image.load('image/TB.png')
    têteG = pygame.image.load('image/TG.png')
    
    corps = pygame.image.load('image/mc.png')
    corpsV = pygame.image.load('image/CV.png')
    
    queue = pygame.image.load('image/q.png')
    queueG = pygame.image.load('image/QG.png')
    queueH = pygame.image.load('image/QH.png')
    queueS = pygame.image.load('image/QS.png')
    
    rotateDB = pygame.image.load('image/RDB.png')
    rotateDH = pygame.image.load('image/RDH.png')
    rotateGB = pygame.image.load('image/RGB.png')
    rotateGH = pygame.image.load('image/RGH.png')

    for k in range (len(S)):
        if (k==0):
            if (S[k][1]==S[k+1][1])&(S[k][0]<S[k+1][0]):
                screen.blit(têteG, S[k])
            elif (S[k][1]==S[k+1][1])&(S[k][0]>S[k+1][0]):
                screen.blit(tête, S[k])
            elif (S[k][0]==S[k+1][0])&(S[k][1]<S[k+1][1]):
                screen.blit(têteH, S[k])
            else:
                screen.blit(têteB, S[k])

        elif ((k!=(len(S)-1))&(k!=0)):
            if (S[k-1][1]==S[k+1][1])|(S[k-1][0]==S[k+1][0]):
                if (S[k][1]==S[k+1][1]):
                    screen.blit(corps, S[k])
                else:
                    screen.blit(corpsV, S[k])
            else:
                if ((S[k+1][1]>S[k][1])|(S[k-1][1]>S[k][1]))&((S[k+1][0]>S[k][0])|(S[k-1][0]>S[k][0])):
                    screen.blit(rotateDB, S[k])
                elif ((S[k+1][1]<S[k][1])|(S[k-1][1]<S[k][1]))&((S[k+1][0]>S[k][0])|(S[k-1][0]>S[k][0])):
                    screen.blit(rotateDH, S[k])
                elif ((S[k+1][1]>S[k][1])|(S[k-1][1]>S[k][1]))&((S[k+1][0]<S[k][0])|(S[k-1][0]<S[k][0])):
                    screen.blit(rotateGB, S[k])
                elif ((S[k+1][1]<S[k][1])|(S[k-1][1]<S[k][1]))&((S[k+1][0]<S[k][0])|(S[k-1][0]<S[k][0])):
                    screen.blit(rotateGH, S[k])

        elif (k==(len(S)-1)):
            if (S[k][1]==S[k-1][1])&(S[k][0]<S[k-1][0]):
                screen.blit(queue, S[k])
            elif (S[k][1]==S[k-1][1])&(S[k][0]>S[k-1][0]):
                screen.blit(queueG, S[k])
            elif (S[k][0]==S[k-1][0])&(S[k][1]<S[k-1][1]):
                screen.blit(queueS, S[k])
            else:
                screen.blit(queueH, S[k])

def affiche_P(S):
    pomme = pygame.image.load('image/pomme.png')
    screen.blit(pomme, S)
Y = []
clientSocket.send(" ".encode())

#La boucle de jeu principale
while True:
    sysFont = pygame.font.SysFont("None", 32)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)

    
    #rendered = sysFont.render('OK', 0, (255,100, 100))
    #screen.blit(rendered, (100, 100))


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                time.sleep(1)
                clientSocket.sendall("U".encode())
                print("Haut")
                
            elif event.key == pygame.K_q:
                time.sleep(1)
                clientSocket.sendall("L".encode())
                print("Gauche")
                
            elif event.key == pygame.K_s:
                time.sleep(1)
                clientSocket.sendall("D".encode())
                print("Bas")
                
            elif event.key == pygame.K_d:
                time.sleep(1)
                clientSocket.sendall("R".encode())
                print("Droite")
                



    pygame.display.flip()
    screen.blit(background,(0,0))

    S = json.loads(clientSocket.recv(1024).decode())
    
    print(S)

    if (S==[0]):
        rendered = sysFont.render('Game over', 0, (255,100, 100))
        print("Tout cassé")
        break

    elif (len(S)==2):
        affiche_P(S)
        Y = S
        pygame.display.update()
        print("La pomme ici")

    else:
        affiche_S(S)
        affiche_P(Y)
        pygame.display.update()
        print("Serpant !")
        
    