def imprimeMensajes():
    print("Esto es un curso de Python")
    print("El curso acaba de empezar")
    print("Python parece interesante")

print("Fuera de la función")

imprimeMensajes()

def devolverMensaje():
    return "Este es el mensajede la función"

print(devolverMensaje())

def saludo(mensaje):
    return "Todo ben, "+mensaje+"?"

print(saludo("Alex"))