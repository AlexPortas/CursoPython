import math
def calculaRaizCuadrada(numero):
    if numero<0:
        raise ValueError("El número no puede ser negativo.")
    else:
        return math.sqrt(numero)

n1 = int(input("Introduce un número: "))

try:
    print(calculaRaizCuadrada(n1))
except:
    print("Error numero negativo.")