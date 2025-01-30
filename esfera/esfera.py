import math

print ("calcular el volumen de una esfera")
print ("para hacer esto, tener en cuenta la formula\n\nV=4/3πr3")

radio = int(input("\nde cuanto es el radio de la esfera?"))
volumen = 4 / 3 * math.pi * (radio*radio*radio)

print (f"el volumen de la esfera es {volumen}")