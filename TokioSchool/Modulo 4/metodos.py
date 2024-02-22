if __name__=='__main__':      
    # string
    print("Hola Mundo".upper(),"Hola Mundo".lower(),"Hola Mundo".capitalize(),"Hola Mundo".title())

    # count(): Devuelve una cuenta de las veces que aparece una subcadena en la cadena

    print("Hola mundo".count('mundo'))

    # find(): Devuelve el índice en el que aparece la subcadena (-1 si no aparece)

    print("Hola mundo".find('mundo'), "Hola mundo".find('mundoz'))

    # rfind():  Devuelve el índice en el que aparece la subcadena, empezando por el final

    print("Hola mundo mundo mundo".rfind('mundo'))

    # isdigit(): Devuelve True si la cadena es todo números (False en caso contrario)

    print("100".isdigit())

    # isalnum(): Devuelve True si la cadena es todo números o carácteres alfabéticos

    print("1111".isalnum())

    # isalpha(): Devuelve True si la cadena es todo carácteres alfabéticos

    print("1210".isalpha(), "Holamundo".isalpha())

    # islower(): Devuelve True si la cadena es todo minúsculas
    # isupper(): Devuelve True si la cadena es todo mayúsculas
    # istitle(): Devuelve True si la primera letra de cada palabra es mayúscula
    # isspace(): Devuelve True si la cadena es todo espacios

    print("  -  ".isspace(), "         ".isspace())

    # startswith(): Devuelve True si la cadena empieza con una subcadena

    print("Hola mundo".startswith("Mola"))

    # endswith(): Devuelve True si la cadena acaba con una subcadena

    print("Hola mundo".endswith('mundo'))

    # split(): Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista

    print("Hola mundo mundo".split()[0], "Hola,mundo,mundo,otra,palabra".split(','))

    # join(): Une todos los caracteres de una cadena utilizando un caracter de unión

    print(",".join("Hola mundo"), " ".join("Hola"))

    # strip(): Borra todos los espacios por delante y detrás de una cadena y la devuelve

    print("   Hola mundo     ".strip(), "-----Hola mundo---".strip('-'))

    # replace(): Reemplaza una subcadena de una cadena por otra y la devuelve

    print("Hola mundo".replace('o','0'), "Hola mundo mundo mundo mundo mundo".replace(' mundo','',3))

    # listas

    # append(): Añade un ítem al final de la lista

    lista = [1,2,3,4,5]
    lista.append(6)
    print(lista)

    # clear(): Vacía todos los ítems de una lista

    lista.clear()
    print(lista)

    # extend(): Une una lista a otra
    l1 = [1,2,3]
    l2 = [4,5,6]
    l1.extend(l2)
    print(l1)

    # count(): Cuenta el número de veces que aparece un ítem

    palabras = ["Hola", "mundo", "mundo"]
    print(palabras.count("mundo"))

    # index(): Devuelve el índice en el que aparece un ítem (error si no aparece)

    print(palabras.index("mundo"))

    # insert(indice, valor): Agrega un ítem a la lista en un índice específico

    nums = [1,2,3]
    nums.insert(0,0)
    print(nums)

    # pop(): Extrae un ítem de la lista y lo borra

    nums.pop() # Extrae el último elemento
    print(nums)
    nums.pop(1) # Extrae el elementos de la posicion 1
    print(nums)

    # remove(): Borra un ítem de la lista directamente

    nums = [10,20,30,40,50]
    nums.remove(30)
    print(nums)

    # reverse(): Le da la vuelta a la lista actual

    nums.reverse()
    print(nums)

    # sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor

    lista = [5,-10,35,0,-65,100]
    lista.sort()
    print(lista)

    lista.sort(reverse=True)
    print(lista)

    # conjuntos (sets)

    # add(): Añade un ítem a un conjunto, si ya existe no lo añade

    c = set()
    c.add(1)
    c.add(2)
    c.add(3)
    print(c)

    # discard(): Borra un ítem de un conjunto

    c.discard(2)
    print(c)

    # clear():  Borra todos los ítems de un conjunto

    c.clear()
    print(c)

    # Comparación de conjuntos

    c1 = {1,2,3}
    c2 = {3,4,5}
    c3 = {-1,99}
    c4 = {1,2,3,4,5}

    # isdisjoint(): Comprueba si el conjunto es disjunto de otro conjunto *Si no hay ningún elemento en común entre ellos*

    print(c1.isdisjoint(c2))

    # issubset(): Comprueba si el conjunto es subconjunto de otro conjunto *Si sus ítems se encuentran todos dentro de otro*

    print(c3.issubset(c4))

    # issuperset(): Comprueba si el conjunto es contenedor de otro subconjunto *Si contiene todos los ítems de otro*

    print(c3.issuperset(c1))

    # union(): Une un conjunto a otro y devuelve el resultado en un nuevo conjunto

    print(c1.union(c2))

    # update(): Une un conjunto a otro en el propio conjunto

    c1.update(c2)
    print(c1)

    # difference(): Encuentra los elementos no comunes entre dos conjuntos

    c1 = {1,2,3}
    c2 = {3,4,5}
    c3 = {-1,99}
    c4 = {1,2,3,4,5}
    print(c1.difference(c2))

    # diccionarios

    colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
    print(colores['amarillo'])

    # get(): Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto

    print(colores.get('negro','no se encuentra'))
    
    # keys(): Genera una lista en clave de los registros del diccionario

    print(colores.keys())

    # values():  Genera una lista en valor de los registros del diccionario

    print(colores.values())

    # items(): Genera una lista en clave-valor de los registros del diccionario

    print(colores.items())

    for c,v in colores.items():
        print(c,v) # clave, valor

    # pop(): Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto

    print(colores.pop("amarillo","no se ha encontrado"))
    print(colores)

    # clear(): Borra todos los registros de un diccionario

    colores.clear()
    print(colores)