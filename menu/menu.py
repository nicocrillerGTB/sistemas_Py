import time

print ("pequeño menu para todas las operaciones")
time.sleep(1)
print ("para empezar,presiona si:\n\n1.sumar\n2.restar\n3.multiplicacion\n4.division")
opc = int(input("="))

if opc == 1 :

    print("para empezar la suma, necesitaré dos numeros")
    time.sleep(1.5)
    print("\ncual es el primer numero?")
    num1 = int(input("="))
    print("dame ahora el segundo")
    num2 = int(input("="))
    time.sleep(1.5)
    print (f"la suma entre {num1} y {num2} es {num1+num2}")
    
elif opc == 2 :

    print ("para empezar a restar, necesitaré los numeros")
    time.sleep (1.5)
    print("\ncual es el primer numero?")
    num1 = int(input("="))
    print("dame ahora el segundo")
    num2 = int(input("="))
    time.sleep(1.5)
    print (f"la resta entre {num1} y {num2} es {num1-num2}")

else :

    if opc == 3 :

        print ("para empezar a multiplicar, necesitaré los numeros")
        time.sleep (1.5)
        print("\ncual es el primer numero?")
        num1 = int(input("="))
        print("dame ahora el segundo")
        num2 = int(input("="))
        time.sleep(1.5)
        print (f"la resta entre {num1} y {num2} es {num1*num2}")
    
    if opc == 4 :

        print ("para empezar a dividir, necesitaré los numeros")
        time.sleep (1.5)
        print("\ncual es el primer numero?")
        num1 = int(input("="))
        print("dame ahora el segundo")
        num2 = int(input("="))
            
        if num2 == 0 :
            print("no se puede dividir por 0 :(")
        else :
        time.sleep(1.5)
        print (f"la resta entre {num1} y {num2} es {num1/num2}")

    else :

        print ("opcion no valida :(")

    