import json

# Diccionarios de las frutas
dicc_frutas_1 = {
    "Nombre": "Manzana",
    "Cantidad": 10
}

dicc_frutas_2 = {
    "Nombre": "Pera",
    "Cantidad": 20
}

dicc_frutas_3 = {
    "Nombre": "Naranja",
    "Cantidad": 30
}

# Diccionario de las verduras
dicc_verduras_1 = {
    "Nombre": "Lechuga",
    "Cantidad": 80
}

dicc_verduras_2 = {
    "Nombre": "Tomate",
    "Cantidad": 15
}

dicc_verduras_3 = {
    "Nombre": "Pepino",
    "Cantidad": 50
}

# Lista de frutas: Contiene los diccionarios de las frutas
lista_frutas = [dicc_frutas_1, dicc_frutas_2, dicc_frutas_3]

# Lista de verduras: Contiene los diccionarios de las verduras
lista_verduras = [dicc_verduras_1, dicc_verduras_2, dicc_verduras_3]

dicc_fruta = {
    "Fruta": lista_frutas
}

dicc_verdura = {
     "Verdura": lista_verduras
}

dicc_fruteria = {
    "Fruteria": [dicc_fruta, dicc_verdura]
}

# Imprimimos por pantalla el tipo y los datos
print(type(dicc_fruteria))
print(dicc_fruteria)

# Nos devuelve el String con el JSON
json_fruteria = json.dumps(dicc_fruteria)

print("Tipo de los datos:", type(json_fruteria))
print("\nDatos en JSON:\n")
print(json_fruteria)

### ¿Diferencias?

print(dicc_fruteria)
print()
print(json_fruteria)

# Disponemos de json_fruteria el cual contiene nuestra informacion en formato JSON
print("Tipo de los datos:", type(json_fruteria))
print("Datos en JSON:\n")
print(json_fruteria)

f_dict = json.loads(json_fruteria)
print("\nTipo de los datos:", type(f_dict))
print("Datos en estructuras de datos de Python (diccionarios):\n")
print(f_dict)

print("Datos completos (tipo ", type(f_dict), ")")
print(f_dict)

print("\nJSON Object Fruta")
print(f_dict['Fruteria'][0]) # JSON Object Fruta
print("\nJSON Object Verdura")
print(f_dict['Fruteria'][1]) # JSON Object Verdura

print("\nJSON Object Fruta. Primer objeto del JSON Array")
print(f_dict['Fruteria'][0]['Fruta'][0]) # JSON Object Fruta. Primer objeto del JSON Array

print("\nNumero de manzanas")
print(f_dict["Fruteria"][0]["Fruta"][0]["Cantidad"]) # Número de manzanas