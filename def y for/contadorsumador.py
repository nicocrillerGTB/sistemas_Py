print ("==============================")
print ("   contador y sumadores")
print ("==============================")
print ("pedir 5 numeros, contar pares e impares y sumar pares e impares")

contador_pares = 0
contador_impares = 0
suma_pares = 0
suma_impares = 0

for i in range (5):
    numero = int(input("dame un numero :: "))
    if numero % 2 == 0:
        contador_pares = contador_pares + 1
        suma_pares= suma_pares + numero
    
    else:
        contador_impares = contador_impares + 1
        suma_impares= suma_impares + numero
print(f"la suma de pares dió {suma_pares} y en total hay {contador_pares} pares")
print(f"la suma de impares dió {suma_impares} y en total hay {contador_impares} impares")
print("fin")