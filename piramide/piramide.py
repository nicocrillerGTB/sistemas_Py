import math, tkinter 

ventana = tkinter()
ventana.title("programa")
ventana.geometry("400x300")
ventana.mainloop()



# codigo principal

print (f"calcular el volumen de una piramide\npara entender esto debemos saber que la formula es V=1/3*l2*h")

l = int(input("\nde cuanto es el lado?"))
h = int(input("de cuanto es la altura?"))

Volumen = 1 / 3 * (l*l) * h

print (f"el volumen de la piramide es de {Volumen}")