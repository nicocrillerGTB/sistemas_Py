print("puedes votar o no?")
print("para saberlo necesitamos un dato")
edad = int(input("cuantos años tienes?"))

if edad > 18 :

    print("tienes la edad apropiada")
    print("bienvenido a la caja de votacion")

elif edad < 18 :

    print("perdon amigo")
    print("no vas a poder votar")

else:

    print("tienes la edad minima")