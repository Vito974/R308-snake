from random import random

class Serpent :
    __position : list
    __direction : str

    def __init__(self):
        self.__position = [[0,0],[1,0],[2,0],[3,0]]
        self.__direction = "R"
   
    def move (self,direction,p) :


        #del self.__position[-1]

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


        else :
            return "error"
        

        #verifie si on est sur la pomme
        if (self.__position[0] != p ):
            del self.__position[-1]


        if (self.__position.count(self.__position[0])> 1) :
            print("game over")
        else :
            print("game continue")
        
        for k in self.__position :
            for e in k :
                if (e > 40 or e < 0) :
                    print("gameover") 

    def get_position(self) :
        return self.__position



class Client :
    __adresse_ip: str
    __port : int
    __serpent : Serpent

    def __init__(self,ip,p,s):
        self.__adresse_ip = ip
        self.__port = p
        self.__serpent = s
    
    def get_position(self) :
        return self.__serpent.get_position()

    def move (self,direction,p) :
        self.__serpent.move(direction,p)

    


class Pomme :
    __position : list
    __serpent : Serpent

    def __init__(self, s):
        self.__position = [random.randrange(0,40),random.randrange(0,40)]
        self.__serpent = s
    
    def position (self):
        return self.__position
    

    def set_position(self) : 
        while (True) :
            self.__position = [random.randrange(0,40),random.randrange(0,40)]
            if (self.__position in self.__serpent.get_position()): 
                continue
            else :
                break
        return self.__position

    

class Server :
    __ip : str
    __port : int


