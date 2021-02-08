paises = {}

pais = input("Introduce un pais: ")

while pais != "Salir":
    ciudad = input("Introduce una ciudad: ")
    
    lista_ciudades = paises.setdefault(pais,[ciudad])
    
    if lista_ciudades != [ciudad]:
        paises[pais].append(ciudad)
    
    pais = input("Introduce un pais: ")

print(paises)