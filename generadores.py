def generaPares(limite):        #funcion
    num = 1
    pares = []
    while num<limite:
        pares.append(num*2)
        num+=1 
    return pares

print(generaPares(6))

def generadorPares(limite):        #generador
    num = 1
    while num<limite:
        yield num*2
        num+=1 

pares = generadorPares(6)

for i in pares:
    print(i)

def capitales(*ciudades):
    for capital in ciudades:
        yield capital
        
capitales = capitales("Berlin", "Roma", "Madrid")

print(next(capitales))

print(next(capitales))

def capitales(*ciudades):
    for capital in ciudades:
        yield from capital
        
capitales = capitales("Berlin", "Roma", "Madrid")

print(next(capitales))

print(next(capitales))