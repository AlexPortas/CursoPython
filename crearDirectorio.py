import os
import io
#os.makedirs('PruebaDirectorio')

os.chdir('PruebaDirectorio')

print(os.getcwd())

f = io.open('archivoPython.txt', 'w')

f.write('Este archivo se creo con Python en este directorio')

f.close()

print(os.listdir('./'))