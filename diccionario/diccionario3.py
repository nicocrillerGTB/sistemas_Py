# Inicio de diccionario - 2 - - - - - - - - - - - -
# dicionario para almacenar usuarios (saquenme de sistemas)

usuario = {}

# definir cuantos usuarios entran
cantidad = 3

# pedir datos y almacenarlos en el diccionario
for i in range (0,cantidad):
    print (f"\ningrese los datos de la persona ({i})")
    nombre = input("\nnombre: ").strip()
    apellido = input("\napellidos: ").strip()
    identificacion = input("\nidentificacion: ").strip()
    usuario[i] = {
        "nombre": nombre,
        "apellido": apellido,
        "identificacion": identificacion
    }

# Mostrar los datos almacenados
print ("\nUsuarioss registrados: ")
for i, datos in usuario.items():
    print (f"persona {i}: {datos['nombre']} {datos['datos']} - ID: {datos['identificacion']}")

for clave, valor in usuario.items():
    print (clave, valor)