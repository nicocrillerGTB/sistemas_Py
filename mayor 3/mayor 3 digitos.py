import time 

print("medir mayor a menor con 3 digitos")
print("para esto necesitamos 3 digitos")

n1 = int(input("el primer numero\n="))
n2 = int(input("el segundo numero\n="))
n3 = int(input("el tercer numero\n="))

if n1 > n2 and n1 > n3 :

    print("el orden esta en que el numero", n1, "es mayor que", n2, "y el numero", n3)

elif n2 > n1 and n2 > n3 :

    print("el orden esta en que el numero", n2, "es mayor que", n3, "y el numero", n1)

else:

    if n3 > n1 and n3 > n2 :

        print("el orden esta en que el numero", n3, "es mayor que", n1, "y el numero", n2)

    elif n1 == n2 == n3 :

        print("los numeros son iguales, no hay mayor ni menor")