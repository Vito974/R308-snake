from Classe import *


client1 = Client("127.0.0.1","3300",Serpent())

print(client1.get_position())

client1.move("D",[0,1])

print(client1.get_position())





"""""
serpent1 = Serpent()

print(serpent1.get_position())

serpent1.move_serpent()

print(serpent1.get_position())
"""""