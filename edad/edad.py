print ("========================")
print ("     calcular edad")
print ("========================")

nombre = "x"
fecha = 0

while nombre != " ":
    nombre = input("dame tu nombre")
    fecha = int(input("año en que naciste"))
    print(f"hola {nombre} tienes {2025-fecha} años")
print ("")