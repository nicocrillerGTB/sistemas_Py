materias=["matemáticas","fisica", "Quimica", "historia", "legunaje"]
for i in materias:
    print(f"yo estudio {i}")

print (materias, end=" ")

for i in range (0,5):
    print (f"yo estudio {materias[i]}")

print (f"el indice de lenguaje es: {materias.index('Lenguaje')}")