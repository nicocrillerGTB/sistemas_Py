# Inicio de diccionario - 4 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Escribir un programa que pregunte al usuario su nombre, edad, direccion y telefono (extraño mi pelo :c )

nom = input("como te llamas? : ")
edad = input("cuantos años tienes : ")
dir = input("cual es tu direccion? : ")
tel = input("cual es tu telefono? : ")
persona = {'nombre': nom, 'edad': edad, 'direccion': dir, 'telefono': tel}

print (persona)
print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su telefono es {persona['telefono']}")