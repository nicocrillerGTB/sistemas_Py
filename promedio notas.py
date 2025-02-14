import math 

print ("= = = = = = = = = = = = = = =")
print ("      promedio de notas     ")
print ("= = = = = = = = = = = = = = =")
print ("para empezar necesitare cuantas\nmaterias tienes")
mat = float(input("\n⊛ cuantas materias son? :: "))
mat_not = 0

while mat != 0 :

    mat_not = float(input("dame la nota :: "))
    print (mat_not, end = (" "))
    mat = mat - 1
