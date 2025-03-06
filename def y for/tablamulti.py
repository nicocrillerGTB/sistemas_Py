print ("========================================")
print ("tablas de multiplicar con un numero dado")
print ("========================================")

num = int(input("daame el numero :: "))
aux = 0

for i in range (-1,9):
    aux += 1 
    print (f"{num} x {aux} = {num*aux}")
