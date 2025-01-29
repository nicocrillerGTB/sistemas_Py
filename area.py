# saludo de inicio

print("calcular area sombreada")

# calculo del lado

lado = int(input("cuanto mide el lado del cuadrado?\n="))
area_c = lado * lado 

# resultado

print(area_c, "es el area del cuadrado")
print("etonces el area de lo sombreado es", area_c*area_c - 3.1416*area_c/2*area_c/2)

