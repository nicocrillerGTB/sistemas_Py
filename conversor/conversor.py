print ("programa conversor")

kelvin = 0

while kelvin == 0 :
    
    kelvin = float(input("introduce temperatura en kelvin"))
    if kelvin == "no":
        break
    celsius = kelvin - 273.15

print (f"{kelvin} grados kelvin son {celsius:.2f} grados celsius")
