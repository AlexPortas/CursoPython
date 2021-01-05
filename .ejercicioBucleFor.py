trabajadores = ["Ana","Luis","Dani"]

trabajadores2 = ["Ana","Luis","samu0"]

frutas = ["Sandia", "Fresa", "Limon"]

edades = [6, 14, 27, 32]

def comparaListas(lista1, lista2):
    if len(lista1)!=len(lista2):
        return False
    else:
        for i in range(1,len(lista1)):
            if lista1[i]!=lista2[i]:
                return False
    return True

print(comparaListas(trabajadores, edades))

print(comparaListas(frutas, edades))

print(comparaListas(trabajadores, frutas))

print(comparaListas(trabajadores, trabajadores2))

print(comparaListas(trabajadores, trabajadores))