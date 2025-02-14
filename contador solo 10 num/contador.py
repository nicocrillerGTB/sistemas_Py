print ("======================")
print (" contador con solo 10")
print ("======================")

cont = 0
x = 1

while x <= 10 :

    num = int(input("dame un numero :: "))

    if (num < 0) :

        print("no se pueden poner negativos")
        break
        
    else :

        cont = cont + 1
        print (x)
        x = x + 1
print (f"entraron {cont} numeros")