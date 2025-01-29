# Uso del If 

import time 

print("VAMOS A LA TIENDA!!!")
print("vas a la tienda a ir por huevos o  por sardinas")
time.sleep (1)
print("*camina*")
time.sleep (1.5)
pr1 = input("el de la tienda: hola, ¿que necesitas?")

# inicio if
if pr1 == "huevos" :

    print("el de la tienda: claro, deja los busco")
    time.sleep (3)
    print("el de la tienda: no vecino, no tengo huevos")
    pr2 = input("que mas quisiera llevar?")

    if pr2 == "sardinas" :

        print("el de la tienda: Claro, de eso si tengo")
        print("fin del programa")
    else: print("el de la tienda: largo de mi tienda")
else: print("el de la tienda: largo de mi tienda")

