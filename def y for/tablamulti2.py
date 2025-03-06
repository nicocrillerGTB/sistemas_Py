print ("========================================")
print ("todas las tablas de multiplicar")
print ("========================================")

x = 0
y = 0

for x in range (10):
    print ("==============")
    print (f"tabla del {x}")
    print ("==============")
    for i in range (10):
        print (f"{x} x {i} = {x*i}") 