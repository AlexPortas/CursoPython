import os
import io

#os.makedirs('PruebaDirectorio2')

os.chdir('PruebaDirectorio2')

print(os.getcwd())

os.rename('renombrado.txt', 'Renombrado.txt')

print(os.listdir('./'))

os.remove('archivoConPython.txt')

print(os.listdir('./'))