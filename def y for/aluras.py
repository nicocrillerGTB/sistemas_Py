print ("=================================")
print ("pedir n alturas y hallar promedio")
print ("=================================")

suma = 0
n = int(input("cuantas alturas? :: "))

for i in range (n) :
    alturas = int(input(f"introduce la altura :: "))
    suma=suma+alturas
print (f"el promedio de alturas fue {suma/n}")
