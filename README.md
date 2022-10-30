# R308-RT2A-snake
Jeu du serpent en python


## PANCHOO-Ashvin-Serveur
Dans cette partie, je vais expliquer la manière dont a été pensé et coder la partie serveur du jeu. Tout d'abord, j'ai créé une branche git serveur dans la quel, j'ai créé le dossier Serveur où j'ai placé les scripts python concernant ma partie. Ensuite, j'ai créé un fichier Class.py qui contient les classes nécessaires pour faire fonctionner le jeu.

## Class Serpent
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

## Class Client
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

## Class Pomme
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



