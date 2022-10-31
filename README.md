# R308-RT2A-snake
Jeu du serpent en python

## NOTICE D'utlisation 
Lancer le script server.py dans le dossier server puis client.py dans le dossier client.

## PANCHOO-Ashvin-YAZGHICH-Zineb - Serveur
Dans cette partie, je vais expliquer la manière dont a été pensé et coder la partie serveur du jeu. Tout d'abord, j'ai créé une branche git serveur dans la quel, j'ai créé le dossier Serveur où j'ai placé les scripts python concernant ma partie. Ensuite, j'ai créé un fichier Class.py qui contient les classes nécessaires pour faire fonctionner le jeu.

### Class Serpent
La classe serpent dispose de deux attributs, une position qui est une liste de la position de chacune des parties du serpent et un attribut direction qui est la direction dans la quel se dirige le serpent. Dans le constructeur de la classe, je mets la position du serpent en ligne droite sur l'axe x avec trois parties du corps ([[0,0],[1,0],[2,0]]) et de plus, il se dirige vers la droite.

```python
class Serpent :
    __position : list
    __direction : str

    def __init__(self):
        self.__position = [[0,0],[1,0],[2,0]]
        self.__direction = "R"
  
```


Je crée aussi l'assesseur qui permet d'obtenir la position du serpent.

```python
def get_position(self) :
        return self.__position
```

Maintenant, je crée la méthode "move" qui permet de déplacer le serpent. Elle prend en argument la direction du serpent (qui serra envoyer par le client à travers le réseau) et la position de la pomme. Pour déplacer le serpent, on fait une copie de la position de la tête du serpent dans la liste, puis on modifie les valeurs de position en fonction de la direction et enfin, on insère cette nouvelle position au début de la liste.

```python
if (direction == "R") :
            pos = self.__position[0].copy()
            pos[0] += 1
            self.__position.insert(0,pos)
        
        elif (direction == "L") :
            pos = self.__position[0].copy()
            pos[0] -= 1
            self.__position.insert(0,pos)

        elif (direction == "U") :
            pos = self.__position[0].copy()
            pos[1] += 1
            self.__position.insert(0,pos)

        elif (direction == "D") :
            pos = self.__position[0].copy()
            pos[1] -= 1
            self.__position.insert(0,pos)
```
Maintenant notre serpent à un élément du corps en plus, il faut donc vérifier si la position de la tête se situe sur la pomme ou non. Si oui alors, on peut laisser notre morceau de serpent en plus, sinon on doit supprimer la queue du serpent pour qu'il reste de la même taille.

```Python
if (self.__position[0] != p ):
            del self.__position[-1]
```

Enfin, nous devons faire en sorte de détecter les collisions avec le bord du plateau et avec le serpent lui-même. Pour ce faire, on utilise la méthode count qui permet de voir si deux éléments identiques sont présents dans la liste. SI c'est le cas cella veut dire que le serpent est revenu sur lui-même donc le jouer à perdu.
```Python
if (self.__position.count(self.__position[0])> 1) :
            print("game over")
        else :
            print("game continue")
```

Pour vérifier si le serpent n'est pas en dehors de la grille, on parcourt toutes les positions de serpent de manière bidimensionnel et on vérifie qu'à aucun moment les valeurs de positions dépasse celle de la taille de la grille.

```Python
 for k in self.__position :
            for e in k :
                if (e > 40 or e < 0) :
                    print("gameover") 
```

### Class Client
Je crée une classe client qui a pour argument une adresse IP, un port et un serpent. Cette classe sera utile si plusieurs clients jouent sur une même grille.
```Python
class Client :
    __adresse_ip: str
    __port : int
    __serpent : Serpent

    def __init__(self,ip,p,s):
        self.__adresse_ip = ip
        self.__port = p
        self.__serpent = s
 
```
On crée deux assesseurs, un pour retourner la position du serpent du client et l'autre pour déplacer le serpent d'un client.

```Python
 def get_position(self) :
        return self.__serpent.get_position()

    def move (self,direction,p) :
        self.__serpent.move(direction,p)
```

### Class Pomme
Enfin, je crée une classe pomme qui prend en argument un serpent et a comme attribut sa propre position. Lors de l'instanciation, on met la position de la pomme dans une position aléatoire sur la grille.

```Python
class Pomme :
    __position : list
    __serpent : Serpent

    def __init__(self, s):
        self.__position = [random.randrange(0,40),random.randrange(0,40)]
        self.__serpent = s
```
Je crée l'assesseur de la position de la pomme.

```Python
 def position (self):
        return self.__position
```
Enfin, je crée la méthode qui permet de replacer la pomme. C'est une boucle qui replace aléatoirement la pomme et qui se termine uniquement quand la nouvelle position de la pomme n'est pas sur le serpent.

```Python
   def set_position(self) : 
        while (True) :
            self.__position = [random.randrange(0,40),random.randrange(0,40)]
            if (self.__position in self.__serpent.get_position()): 
                continue
            else :
                break
        return self.__position
 ```
## NANY-ANDIAPIN Emerick ISAMBERT Gabriel - Client 
Dans cette partie, je vais expliquer la manière dont a été pensé et coder la partie serveur du jeu. Tout d'abord, j'ai créé une branche git client dans laquel, j'ai créé le dossier Client où j'ai placé les scripts python concernant ma partie.

### Fonction Affiche_S (affiche serpent)
Cette fonction a pour but d'afficher le serpent qui de base se trouve être une liste de coordonnées.

Dans un premier temps nous commencerons par chargé tous les sprites pour l'utilisation de la fonction.

```Python
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
```

Par la suite en fonction des coordonnées noté k, de la suite des coordonnés (k+1) et par moments d'ancien coordonné (k-1) j'ai pu définir les règles pour la sélection du sprite à afficher en fonction des coordonnées. Et j'ai mis toutes les règles dans une boucle qui parcourt toute la liste.

```Python
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
```

Voilà maintenant nous avons une fonction qui est capable d'afficher un serpent à partir d liste !

### Fonction Affiche_P (affiche Pomme)

La fonction affiche pomme est une fonction simple qui permet d'afficher une pomme en fonction d'une liste simple composée de deux nombres (coordonnée). Dans un premier temps nous chargons le sprit de la pomme dans le programme, puis nous l'affichons à l'endroit donné dans la liste.

```Python
def affiche_P(S):
    pomme = pygame.image.load('image/pomme.png')
    screen.blit(pomme, S)
```

### La détection des touches !

Pour la détection des touches appuyées pendant les jeux nous utiliseront la variable EVENT de pygame pour détecter les quatre touches (Z Q S D) de déplacement pour le serpent. Quand une des touches est appuyée, cela enverra au serveur une lettre au serveur pour le notifier du changement de direction du serpent.

```Python
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
```

### Le traitement des listes envoyé par le serveur !
Différentes listes sont envoyé par le serveur, une liste simple avec juste deux coordonné pour la pomme, une liste longue avec 3 ou plus de 3 coordonnés pour le serpent, ou encore une liste vide quand on atteint le GAME OVER !

Il faut donc traité et géré toutes ces listes pour faire fonctionner le jeu. 
En fonction de la longueur de la liste nous pouvons donc savoir à quoi vas servir cette liste et l'utiliser avec la fonction appropriée !

```Python
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
```
