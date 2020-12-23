import math

contador=1
while contador<10:
    print(str(contador)+" vez")
    if contador==5:
        break
    contador=contador+1

print("Fuera del bucle")

edad=int(input("Introduce tu edad: "))

while edad>64 or edad<18:
    print("Edad incorrecta")
    edad=int(input("Introduce tu edad: "))

if edad>=18:
    print("Puedes pasar, gracias!")

print("Tu ed<ad es "+str(edad))

print("Vamos a hallar la raiz cuadrada de un numero")

numero=int(input("Introduce un numero: "))

intentos=1

while numero<0:
    print("El número no puede ser negativo")
    numero=int(input("Introduce un número: "))
    intentos=intentos+1
    if intentos==3:
        break

if intentos<3:
    print("La raiz cuadrada es "+str(math.isqrt(numero)))
else
    print("Intentelo más tarde")