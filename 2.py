#importando cosas
import time

# inicio
entrada = input("pon un numero dependiendo a que vas a entrar\npresione <1> para saber tu nombre\npresione <2> para adivinar un numero\npresione <3> si quieres usar una calculadora basica\n\n numero:")

#lo del nombre
if entrada == 1 :

    nombre = input("dame tu nombre")
    apellido = input("dame tu apellido")
    edad = input("dame tu edad")
    print("hola", nombre,"su apellido es", apellido, "y su edad", edad ,"años*2")
f

# otra conversacion
if entrada == 2 :

    time.sleep(1)
    print("ok espera...")
    time.sleep(2)
    numero = input("dame un numero aleatorio")
    print("procesando....")
    time.sleep(1)
    print("leyendo mente....")
    time.sleep (5)
    print("tu numero es", numero)


# calculadora
if entrada == 3:

    print("programa para sumar :D")
    time.sleep (2)
    que_hacer = input("para sumar presione < 1 >, para restar presione <2>, para multiplicar presione <3> y para dividir <4> ")

    if que_hacer == 1 :
    
        print("suma")

        num1 = input("da un numero para sumar")
        num2 = input("da el segundo numero para sumar")
        print("el resultado de la suma entre", num1, "y", num2, " es", num1+num2)

    if que_hacer == 2 :

        num1 = input("da un numero para restar")
        num2 = input("da el numero que resta al primer numero")
        print("la resta entre", num1, "y", num2, "es", num1-num2)
    
    if que_hacer == 3 :

        num1 = input("da el numero a multiplicar")
        num2 = input("dame el numero que multiplica")
        print("la multiplicacion entre", num1, "y", num2, "es", num1*num2)
    
    if que_hacer == 4 :

        num1 = input("de el numero para dividir")
        num2 = input("da el numero que divide")
        print("la division entre", num1, "y", num2, "es", num1/num2)

    



