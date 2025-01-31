import math, time, random

print ("┏          ┓\n  Proyecto\n┗          ┛\n\nBienvenido a mi programa, en este podrás hacer diferentes cosas\ndependiendo del numero que pongas")
time.sleep (0.5)
print ("\n1.saludar\n2.calculadora\n3.adivinador de numero\n4.conversor\n5.mayor y menor")

opc_men = int(input("\n:: numero ::"))

if opc_men == 1 :

    time.sleep (0.3)
    print ("para iniciar esto, necesitare algunos datos")
    time.sleep (1.2)
    nom = input("dame tu nombre")
    apl = input("dame tu apellido")
    edad = input("dame tu edad")
    pais = input("en donde vives?")
    prof = input("cual es tu profecion?")
    time.sleep (1.2)
    print (f"oh, hola {nom} {apl}, tienes {edad} años, segun vives en {pais} y eres un/a {prof}, un gusto conocerte :)")

if opc_men == 2 :

    time.sleep (0.5)
    print ("┏             ┓\n  calculadora\n┗             ┛\n\n Para iniciar, debes de darme un numero del 1 al 4 dependiendo de que quieres hacer")
    print ("\n1.sumar\n2.restar\n3.multiplicar\n4.dividir")

    opc_cal = int(input("\n:: numero ::"))

    if opc_cal == 1 :

        time.sleep (0.3)
        print ("para empezar necesiaré 2 numeros")
        time.sleep (1)
        num1 = int(input("dame el primer numero"))
        num2 = int(input("dame el segundo numero"))
        time.sleep (0.3)
        print (f"el resultado es {num1 + num2}")


    if  opc_cal == 2 :

        time.sleep (0.3)
        print ("para empezar necesiaré 2 numeros")
        time.sleep (1)
        num1 = int(input("dame el primer numero"))
        num2 = int(input("dame el segundo numero"))
        time.sleep (0.3)
        print (f"el resultado es {num1 - num2}")

    if  opc_cal == 3 :

        time.sleep (0.3)
        print ("para empezar necesiaré 2 numeros")
        time.sleep (1)
        num1 = int(input("dame el primer numero"))
        num2 = int(input("dame el segundo numero"))
        time.sleep (0.3)
        print (f"el resultado es {num1 * num2}")

    if  opc_cal == 4 :

        time.sleep (0.3)
        print ("para empezar necesiaré 2 numeros")
        time.sleep (1)
        num1 = int(input("dame el primer numero"))
        num2 = int(input("dame el segundo numero"))
        time.sleep (0.3)
        if num2 == 0 :

            time.sleep (0.4)
            print("no puedes dividir entre cero :(")
        else:

            print(f"el resultado es {num1 / num2}")

if opc_men == 3 :

    time.sleep (0.3)
    print ("┏                 ┓\n  adivinar numero\n┗                 ┛\n\n'adivinare tu numero diciendo algunos aleatorios")
    time.sleep (0.3)
    print ("las reglas son simples, yo doy un numero del 1 al 10, si lo logras adivinar\nganas, pero, si fallas 3 veces, pierdes")
    num_alt_bot = random.randint(1,10)
    


    time.sleep (0.3)
    num_alt_1 = int(input("primer intento ="))
        
    if num_alt_1 == num_alt_bot :

        print ("LO ADIVINASTE :DD !!!")

    elif num_alt_1 > 10 : 

        print ("no te pases de listo, perdiste")


    else:

        print("buen intento...")
        time.sleep (0.3)
        num_alt_2 = int(input("segundo intento"))   

        if num_alt_2 == num_alt_bot :

            print("lo lograste :D !!")
        elif num_alt_2 > 10 :

            print ("no te pases de listo, perdiste")

        else:

            print("que mal, no es el numero...")
            num_alt_3 = int(input("ultimo intento..."))

            if num_alt_3 == num_alt_bot :

                print(f"LA TERCERA ES LA VENCIDA >:DD, el numero era {num_alt_bot}")
            elif num_alt_3 > num_alt_bot :

                print ("no te pases de listo, perdiste")
            else: 
                print(f"perdiste :( , el numero era {num_alt_bot}, intentalo para la proxima")
            

if opc_men == 4 :

    time.sleep (0.3)
    print ("┏                                        ┓\n  conversor de pesos a dolares y a euros\n┗                                        ┛")
    print ("sencillo, un conversor de pesos a dolares, y de dolares a euros")
    time.sleep (0.3)
    # importo tiempo

    print("para la conversion, debes tener en cuenta que el dolar esta a 4.300")

    time.sleep (1.5)

    presio_dolar = 4300
    pesos = int(input("cuantos pesos tiene??"))
    dolares = pesos / presio_dolar

    print(pesos, "pesos colombianos estan a", dolares, "dolares")
    time.sleep (1.5)


    yn = input("desea cambiar los dolares a euros?\nY = si\nN = no\n=")

    if yn == "Y" or "y" :

        presio_euro = 0.96    
        euros = dolares / presio_euro
        print(dolares, "dolares, son", euros, "euros")
    else: print("fin del programa")

if opc_men == 5 :


    print ("para empezar, necesito los 2 numeros para ver quien es mayor y quien es menor")
    time.sleep (0.3)
    mm1 = int(input("primer numero\n::"))
    mm2 = int(input("segundo numero\n::"))
    time.sleep (0.3)
    
    if mm1 > mm2 :
    
        print(f"es mayor {mm1} que {mm2}")
    
    elif mm1 < mm2 :

        print(f"es mayor {mm2} que {mm1}")
    else: 

        print(f"los numeros son iguales")

if opc_men > 5 :

    print ("no esta esa opcion")