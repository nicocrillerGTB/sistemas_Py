print ("=================================================")
print ("\nhallar los multiplos de 7 desde dos numeros dados\n")
print ("=================================================")

x = int(input("primer numero"))
y = int(input("segundo numero"))

for i in range (x,y):
    if i % 7 == 0:
        print (i,end=" ")
print("fin")