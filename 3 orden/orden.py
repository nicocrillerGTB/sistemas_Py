print ("Programa para saber si es un triangulo o no")
print ("para ello vamos a trabajar primero con los\ndatos que des")
print ("===========================================")

a = int(input("dame un lado" ))
b = int(input("\ndame el otro lado "))
c = int(input("\ndame el ultimo lado "))
aux = ()

if a > b :

    aux = a
    a = b 
    b = aux

if a > c :

    aux = a
    a = c
    c = aux

if b > c :    

    aux = b
    b = c
    c = aux

print (f"el orden es {a, b, c}")