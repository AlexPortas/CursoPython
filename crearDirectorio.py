import os

os.chdir('PruebaDirectorio2')

print(os.getcwd())

os.remove('Renombrado.txt')

os.remove('archivoPython.txt')

print(os.listdir('./'))

os.chdir('..')

os.rmdir('PruebaDirectorio2')