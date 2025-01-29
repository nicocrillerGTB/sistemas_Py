print("bienvenido a la estacion de vacunas")
print("para saber si te puedes vacunar necesitaremos tu edad")

edad = int(input("pon tu edad aqui\n="))

if edad < 10 or edad > 70 :

    print(f"lo lamento, pero la edad de {edad} años no esta permitida para vacunarse" )

elif edad > 10 or edad < 70 : 

    print(f"tu edad es perfecta para vacunarse")