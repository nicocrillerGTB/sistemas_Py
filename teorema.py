import math

print("==============================")# 30
print("calcular teorema de pitagoras")
print("==============================")
print("¿que es lo que vamos a hallar?\n\nh :: altura\na :: cateto\nb :: base")

hallar = input("\n::")

if hallar == "h" or "altura" :

    print("==============================")

    b = int(input("dame la base (b)"))
    a = int(input("dame el cateto (a)"))

    h = math.sqrt (a**2 + b**2)

    print("==============================")
    print(f"la altura es de {h}")
    print("==============================")


elif hallar == "a" or "cateto" :

    print("==============================")

    h2 = int(input("dame la altura(h)"))
    b2 = int(input("dame la base (b)"))

    a2 = math.sqrt (h2**2 - b2**2)

    print("==============================")
    print(f"el cateto es {a2}")
    print("==============================")
    
