# insertar dato (siempre str)

print(input("Introduce dato:"))

# introducir varios valores

valores = []
print("Introduce 3 valores")
for x in range(3):
    valores.append( input("Introduzca un valor: ") )
print(valores)

# print

v = "otro texto"
n = 10
print("Un texto",v,"y un número",n)

# sep y end

print(1, 2, 3, 4, sep=', ')
print(1, 2, 3, 4, sep=', ', end='...\n')

# format

c = "Un texto {} y un número {}".format("texto",54)
print(c)