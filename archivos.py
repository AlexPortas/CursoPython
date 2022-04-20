from io import open     

f = open('primerArchivo.txt', 'r')

print(f.read())

f.seek(0)

#f.seek(len(f.read())/2)

f.seek(len(f.readline()))

print(f.read())

f.close()