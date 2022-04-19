from io import open     

f = open('primerArchivo.txt', 'r')

#f.write('\n añadir linea con python')
info = f.read()

f.close()

print(info)