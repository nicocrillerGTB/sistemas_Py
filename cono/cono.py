import math

print("volumen de un cono\npara saber como se hace, la formmula seria v= 1/3 * pi*r2*h")

h  = int(input("dame la altura"))
r  = int(input("dame el radio"))

resultado = 1/3*math.pi*(r*r)*h

print(f"el volumen del cono es {resultado}")