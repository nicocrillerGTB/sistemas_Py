materias=["matemáticas","fisica", "Quimica", "historia", "legunaje"]
notas=[]
for i in materias:
    nota=float(input(f"que nota sacase en ? {i}"))
    notas.append(nota)
for i in range(len(materias)): # definicion len - longitud de la variable (materias)
    print(f"en {materias[i]} has sacado {i}")