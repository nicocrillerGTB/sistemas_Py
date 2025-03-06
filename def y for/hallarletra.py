print ("============================================")
print ("cuantas veces aparece una letra en una frase")
print ("============================================")
frase = input("introduce una frase: ")
letra = input("introduce la letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print (f"la letra {letra} aparece {contador} veces en la frase: {frase}")