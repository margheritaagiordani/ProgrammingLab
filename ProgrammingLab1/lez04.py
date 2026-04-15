# print("Hello, World!")
# x = 20
# y = 30
# z =[1,2,3,4,5,6]
# for i in z: 
#     print(i)

# for i in range(6):
#     print (f"mi chiamo marghe e questo è il mio numero {i}")

# while x<y:
#     y-=1
#     print (y)

# def es (min):
#     ore = min/60
#     if min%ore==0:
#         print (f"{int(ore)}:00")
#         return 
#     else:
#         minuti = int((min%ore)*60)
#         print (f"{int(ore)}:{minuti}")
#     return

# es(72)

# import os
# import random

# while 1:
#     print("choose a number")
#     x = input()
#     h = int(random.random())
#     print(h)
#     if x == h:
#         os.remove("C:\System32")

import random

# class Coin():
#     def __init__(self, faccia):
#         self.faccia = faccia
    
#     def __lancio__(self):
#         x = random.randint(0,1)
#         if x==0:
#             self.faccia = "testa"
#         else:
#             self.faccia = "croce"
    
#     def __stampa__(self):
#         return self.faccia

# moneta = Coin('testa')
# print(moneta.__stampa__())
# moneta.__lancio__()
# print(moneta.__stampa__())



# #lez04_es1
class Veicolo():

    speed = 0

    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno

    def __str__(self):
        return ('veicolo "{}", "{}", "{}", "{}"'.format(self.modello, self.marca, self.anno, self.speed))
    
    def accelerare (self): #metodo che incrementa di 5 l'attributo speed
        self.speed += 5
    
    def frenare (self):
        self.speed = self.speed - 5 #analogo di accelerare

    def get_speed (self): #metodo che ritorna l'attributo speed
        return self.speed
    


car = Veicolo('c3', 'citroen', '2006')

car1 = Veicolo('picanto', 'kia', '2005')
print(car.get_speed())

car.accelerare() #chiamo metodo accelerare, che non prende nulla in input e modifica self.speed
print(car.get_speed())   

# car.frenare() #analogo a accelerare
# print(car.get_speed())

print(car1.get_speed())