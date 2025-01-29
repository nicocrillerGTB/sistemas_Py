# importo tiempo

import time

# el dolla esta a 4.300 entonces...

print("para la conversion, debes tener en cuenta que el dolar esta a 4.300")

time.sleep (1.5)

presio_dolar = 4300
pesos = int(input("cuantos pesos tiene??"))

dolares = pesos / presio_dolar

print(pesos, "pesos colombianos estan a", dolares, "dolares")

time.sleep (1.5)

# pregunta

yn = input("desea cambiar los dolares a euros?\nY = si\nN = no\n=")

if yn == "Y" or "y" :

    presio_euro = 0.96
    
    euros = dolares / presio_euro

    print(dolares, "dolares, son", euros, "euros")
else: print("fin del programa")

