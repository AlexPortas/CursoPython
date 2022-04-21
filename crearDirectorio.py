import os
import io

os.makedirs('PruebaDirectorio2')

os.chdir('PruebaDirectorio2')

print(os.getcwd())

f = io.open('archivoPython.txt', 'w')

f.write('Este archivo se creo con Python en este directorio')

f.close()

f = io.open('archivoConPython.txt', 'w')

f.write('Este archivo se creo con Python en este directorio')

f.close()

f = io.open('archivoPrueba.txt', 'w')

f.write('Este archivo se creo con Python en este directorio')

f.close()

print(os.listdir('./'))