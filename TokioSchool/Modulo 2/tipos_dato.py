# Utilizando el intérprete como una calculadora

print(3+2, 3-2, 3*2, 3/2, 3%2, 3**2)

# Complex: Números compuestos de una parte real y una parte imaginaria

print(4+5j)

# asignación multiple

x,y= 20,5
print(x, y)

# end

a="una cadena"
b="otra cadena"

print(a)
print(b)
print(a, end="")
print(b)
print(a, end=", ")
print(b)

# salto de linea y tabulador

print("Este es un texto de prueba"+"\ncon un salto de linea"+"\t con un tabulador")

# multiplicar cadenas

diez_espacios = " " * 10
print(diez_espacios + "un texto a diez espacios")

# Slicing

palabra = "Python"
print(palabra, palabra[2:], palabra[:4], palabra[1:3], palabra[-1], palabra[-4:-2])

# negar un bool

print(not True)