import random

print("Vamos a hallar un número aleatorio entre 1 y 100")

numeroAleatorio=random.randint(1,100)

numero=int(input("Introduce un numero: "))

intentos=1

while numero!=numeroAleatorio:
    if 0<numero<100:
        if numeroAleatorio<numero:
            print("El número desconocido es menor que "+str(numero))
        else:
            print("El número desconocido es mayor que "+str(numero))
        numero=int(input("Introduce un número: "))
        intentos=intentos+1
    else:
        print("El número introducido no está entre 1 y 100")
        numero=int(input("Introduce un número: "))
        intentos=intentos+1

print("Lo has consegido. Has necesitado "+str(intentos)+" intentos.")
