import csv

# Leer archivo csv con reader
with open("02_CSV_data.csv", "r") as my_csv_file:
    reader = csv.reader(my_csv_file)
    for row in reader:
        print ( row )

# Leer archivo csv con reader y optimizando la salida
with open("02_CSV_data.csv", "r") as my_csv_file:
    reader = csv.reader(my_csv_file, delimiter=',')
    for row in reader:
        print ( row )

# Uso de reader y next

# Leer archivo csv con reader y next
with open("02_CSV_data.csv", "r") as my_csv_file:
    reader = csv.reader(my_csv_file, delimiter=',')
    reg0 = next(reader)  # Leer registro (lista)
    print(reg0)  # Mostrar registro
    reg1 = next(reader)  # Leer siguiente registro (lista)
    print(reg1)  # Mostrar registro
    nombre, provincia, consumo = next(reader) # Almacenar en variables el siguiente registro (en el orden que se indica)
    print(nombre, provincia, consumo) # Mostrar las variables

# Leer archivo csv con reader, next, bucle y formato de salida
with open("02_CSV_data.csv", "r") as my_csv_file:
    reader = csv.reader(my_csv_file, delimiter=',')
    next(reader) # Saltarnos la cabecera del documento CSV
    for index,row in enumerate(reader):
        print('Linea: ' + str(index))
        print('Nombre: ' + row[0] + ', Provincia: ' + row[1] + ', Consumo: ' + row[2])

# Ordenacion por campos con operator
        
import operator
# Leer archivo csv con reader y mostrarlo ordenado por el segundo campo (provincia)
my_csv_file = csv.reader(open("02_CSV_data.csv"))
listaordenada = sorted(my_csv_file,
                       key=operator.itemgetter(2),
                       reverse=False)
for i in listaordenada:
    print(i)

# Leer archivo csv como lista de diccionarios con DictReader() y mostrar sólo datos de algunas columnas
with open("02_CSV_data.csv") as my_csv_file:
    reader = csv.DictReader(my_csv_file)
    for reg in reader:
        print(reg['provincia'], reg['consumo'])

# Leer archivo csv como lista de diccionarios y obtener una lista ordenada descendente por el campo 'consumo'
my_csv_file = open("02_CSV_data.csv")
reader = csv.DictReader(my_csv_file)
listadicc = list(reader)  # Obtener lista de diccionarios
listafinal = sorted(listadicc,
                      key=operator.itemgetter('consumo'),
                      reverse=True)
for registro in listafinal:
    print(registro)

# Borrar y cerrar fichero csv
with open("02_CSV_data.csv", "r") as my_csv_file:
    reader = csv.reader(my_csv_file)
    for row in reader:
        print ( row )

del reader  # Borrar objetos
my_csv_file.close()  # Cerrar archivo
del my_csv_file  # Borrar objeto
print("Fichero csv cerrado con éxito")

# Escribir todas las tuplas de una lista con writerow() y writerows() en un fichero nuevo (apertura del fichero con "w" o "wb")
datos = [('aaa', 111),('bbb', 222),('ccc', 333)]
csvsalida = open("02_CSV_data_2.csv", "w", newline='')
writer = csv.writer(csvsalida)
writer.writerow(['campo1', 'campo2'])
writer.writerows(datos)

del writer
csvsalida.close()

# Añadir todas las tuplas de una lista en un fichero existente (apertura del fichero con "a" o "ab", que viene de append y añade info al final)

datosNuevos = [('ddd', 444), ('eee', 555), ('fff', 666)]
csvsalida = open("02_CSV_data_2.csv", "a", newline='') # a de append
writer = csv.writer(csvsalida)
writer.writerows(datosNuevos)

del writer
csvsalida.close()