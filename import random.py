# import nuevo aprendido: import random, sys, time
# "sys" es para importar termcolor, y de ahí importo colored y cprint
# con cprint puedo imprimir una linea entera con el color que to quiera
# y usando attrs=[] le puedo poner un atributo, ya sea blond (para negrilla) entre otros

import random, sys, time
from termcolor import colored, cprint

opc1 = colored("1.", "red")
opc2 = colored("2.", "red")


cprint ("============================","red")
cprint ("\nnumeros aleatorios\n","red",attrs=["bold"])
cprint ("============================","red")
print (f"para poner en practica el import nuevo, selecciona que quieres hacer\n\n{opc1} jugar a numeros aleatorios\n{opc2} ver funcion de todos los metodos")

opc = int(input("\n:: "))

if opc == 1 :

    cprint ("=======================","red")
    cprint ("\nadivina el numero\n","red",attrs=["bold"])
    cprint ("=======================","red")
    print ("tienes 3 oportunidades para adivinar el numero del 1 al 10")
    vid = 3 
    num_alt = random.randint(1,10)

    while vid > 0 :
        num = int(input("\npon un numero (1-10)\n:: "))
    
        if num == num_alt :
            print (f"\ncorrecto, el numero es {num_alt}")
            cprint ("fin","red")
            break
        elif True :
            print ("ese no es el numero correcto\n")
            vid = vid - 1
        if vid == 0 :
            print (f"fallaste, el numero correcto era {num_alt}")
            cprint ("fin","red")
            break

if opc == 2 :
    cprint ("=======================","red")
    cprint ("\nfunciones de import random\n","red",attrs=["bold"])
    cprint ("=======================","red")

    x = random.uniform (1,10)
    x2 = random.randrange (1,10)
    print (x, ",con random.uniform podemos generar numeros aleatorios con decimal")
    time.sleep (1)
    print (x2, ",con random.randrange podemos generar un numero aleatorio de los datos que demos")
    time.sleep (1)
    print ("estos son algunos que nos han enseñado")
    cprint ("fin.", "red")
