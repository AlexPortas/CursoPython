'''
Lista []  Colección ordenada y modificable. Permite miembros duplicados.
Tupla () Colección ordenada e inmutable. Permite miembros duplicados.
Set {} Colección desordenada y no indexada. No hay miembros duplicados.
Diccionario {}  Colección desordenada, modificable e indexada. No hay miembros duplicados.
'''

# lista

datos = [4,"Una cadena",-15,3.14,"Otra cadena"]
print(datos)

# agregar a lista

datos.append(True)
datos.insert(0, 7)
print(datos)

# buscar en lista

print(4 in datos)

#contar valores lista

print(len(datos))

#tupla

datos = (4,"Una cadena",-15,3.14,"Otra cadena")
print(datos)

# iguales a las listas pero no son modificables

# conjuntos

datos = {4,"Sarai",-15,3.14,"Alex"}
alumnos = {"Alex","Sarai","Sestelo","Iris"}
print(datos, alumnos)

# sin indice, así que no se puede modificar pero si añadir

alumnos.add( "Breixo")
print(alumnos)

# no se puede duplicar un valor

alumnos.add( "Alex")
print(alumnos)

# eliminar valores

lenguajes = {'C#', 'Python', 'Go', 'C++', 'Javascript', 'Java', 'PHP'}
lenguajes.remove("Go")
lenguajes.discard("PHP")
elementoExtraido = lenguajes.pop() # Pop extrae y elimina un elemento aleatoriamente
print("Elemento extraido con pop: ", elementoExtraido)
print(lenguajes)

# union

print(datos | alumnos)

# intersección

print(datos & alumnos)

# negacion

print(datos - alumnos, alumnos - datos)

# diccionarios

vehiculos = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(vehiculos)

# agregar elementos

vehiculos["color"] = "red"
print(vehiculos)

# eliminar elementos

vehiculos.pop("model")
print(vehiculos)