# if

n = 11
if n % 2 == 0:
    print(n,"es un número par")
else:
    print(n,"es un número impar")

nota = float(input("Introduce una nota: "))
if nota >= 9 and nota < 10:
    print("Sobresaliente")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 5 and nota < 6:
    print("Suficiente")
elif nota < 5 and nota >0:
    print("Insuficiente")
else:
    print("Valor incorrecto.")

# while
    
c = 0
while c <= 2:
    c+=1 
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)

# continue y break
    
c = 0
while c <= 5:
    c+=1
    if c==2:
        print("Continuamos con la siguiente iteración",c)
        continue
    if c==4:
        print("Rompemos el bucle cuando c vale",c)
        break
    print("c vale",c)

# for
    
numeros = [1, 2, 3, 4, 5]
for indice,numero in enumerate(numeros):
    print(indice, "->", numero)

# range 
    
for i in range(4):
    print("Esta es la vuelta", i)

# recorrer diccionario
    
vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for i in vehiculos.values():
    print(i)
for x,y in vehiculos.items():
    print(x, "->", y)