print("=========================")
print("\n  calcular altura de\n      5 alumnos\n")
print("=========================")

suma = 0
x = 1

while x<=5 :

    altura = int(input("dame la altura"))
    suma = suma+altura
    x = x+1
print (f"el promedio es de {suma/x}")