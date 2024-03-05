# Creación de ficheros y escritura

texto = "Una línea con texto\nOtra línea con texto"

fichero = open("01_fichero.txt","w")  # 01_fichero.txt ruta donde lo crearemos, w indica modo de escritura, write

fichero.write(texto) # Escribimos el texto. El numero que aparece con esta operacion es el numero de caracteres

fichero.close()  # Cerramos el fichero

# Lectura de un fichero de texto

fichero = open("01_fichero.txt","r")  # Modo lectura read, por defecto ya es r, no es necesario

texto = fichero.read() # Lectura completa

fichero.close()

print(texto)

fichero = open("01_fichero.txt","r")
texto = fichero.readlines() # Leer creando una lista de líneas
fichero.close()
print(texto)

print(texto[-1]) # Última línea (accedemos como una lista normal)

# Añadir contenido al fichero (al final)

fichero = open("01_fichero.txt","a")  # Modo a, append, añadir

fichero.write('\nOtra línea más abajo del todo')

fichero.close()

#Volvemos a leer el fichero para comprobar que se haya añadido esta tercera línea

fichero = open("01_fichero.txt","r")
texto = fichero.readlines() # Leer creando una lista de líneas
fichero.close()
print(texto)

# Lectura de un fichero no existente y creación automática

fichero = open("01_fichero_inventado.txt","a+")  # Extensión con escritura simultánea, crea fichero si no existe
fichero.close()

# Lectura línea a línea

fichero = open("01_fichero.txt","r")

print(fichero.readline())   # Línea a línea

print(fichero.readline())

print(fichero.readline())

print(fichero.readline())

fichero.close()

# Lectura línea a línea secuencial

with open("01_fichero.txt","r") as fichero:
    for linea in fichero:
        print(linea)