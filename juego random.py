import time
import random

sure = "n"

print ("Juego de dados")
     
while sure == "n" :
    print ("\nlas reglas son sencillas, un bot va a tirar los dados y\napenas acabe debes de tirar tus dados, el que la suma\nde dados sea mas grande gana (5 dados cada uno)")
    sure = input("¿entendiste? (y/n)\n")    


print ("- - - - - - - - - -")
print ("  turno del bot")
print ("- - - - - - - - - -")
time.sleep (1.5)
print ("tirando dados...")
time.sleep (1.5)
numbot1 = random.randrange (2,6)
print (f"\nel primer numero del bot es {numbot1}")
time.sleep (1.5 or 2 or 3)
numbot2 = random.randrange (1,6)
print (f"el segundo numero del bot es {numbot2}")
time.sleep (1.5 or 2 or 3)
numbot3 = random.randrange (1,6)
print (f"el segundo numero del bot es {numbot3}")
time.sleep (1.5 or 2 or 3)
numbot4 = random.randrange (1,6)
print (f"el segundo numero del bot es {numbot4}")
time.sleep (1.5 or 2 or 3)
numbot5 = random.randrange (1,6)
print (f"el segundo numero del bot es {numbot5}")
sumdadbot = numbot1+numbot2+numbot3+numbot4+numbot5
print (f"la suma de los dados del bot es {sumdadbot}")
print ("- - - - - - - -")
print ("   tu turno")
print ("- - - - - - - -")
ent = input("presiona enter para tirar el primer dado")
print ("tirando....")
time.sleep (1.5 or 2)
num1 = random.randrange (1,6)
print (f"el primer numero dió {num1}")
ent = input("presiona enter para tirar el segundo dado")
print ("tirando....")
time.sleep (1.5 or 2)
num2 = random.randrange (1,6)
print (f"el segundo numero dió {num2}")
ent = input("presiona enter para tirar el tercer dado")
print ("tirando....")
time.sleep (1.5 or 2)
num3 = random.randrange (1,6)
print (f"el tercer numero dió {num3}")
ent = input("presiona enter para tirar el cuarto dado")
print ("tirando....")
time.sleep (1.5 or 2)
num4 = random.randrange (1,6)
print (f"el cuarto numero dió {num4}")
ent = input("presiona enter para tirar el quinto dado")
print ("tirando....")
time.sleep (1.5 or 2)
num5 = random.randrange (1,6)
print (f"el quinto numero dió {num5}")
sum = num1+num2+num3+num4+num5
print (f"la suma de tus dados dió {sum}")
if sum > sumdadbot :
    print ("tu suma es mayor que la del bot, ganas")
if sum < sumdadbot :
    print ("la suma del bot es mayor que tu suma, pierdes")
if sum == sumdadbot:
    print ("tu suma es igual a la del bot, empate")
print ("fin del programa")