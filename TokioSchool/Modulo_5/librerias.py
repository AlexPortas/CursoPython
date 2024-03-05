# pip install matplotlib
# pip install pandas
# pip list
# NumPy

import numpy as np
# Para ver la versión que tenemos instalada:
print(np.__version__)
nums = [1, 2, 3, 4]
array = np.array(nums) 
print(array)
print(type(array))
print(array.dtype)

# Array de dos dimensiones
array2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]) 
print(array2)

# Suma
print(np.sum(array))

# Máximo
print(np.max(array))

# Seno
print(np.sin(array2))

print(np.pi)
print(np.e)

# array de ceros

# En una dimensión
a = np.zeros(14)
print(a)

# En dos dimensiones
a = np.zeros([4,10])
print(a)

# array de unos
a = np.ones([3, 2])
print(a)

# array identidad
a = np.identity(5)
print(a)

# Rangos
a = np.arange(0, 11, 3) #inicio, fin, salto
print(a)

# np.linspace
a = np.linspace(0, 20, 10) # inicio, fin, num_resultados
print(a)

# reshape
a = np.arange(1, 11)
m = np.reshape(a, [5, 2])
print(m)

# También funciona como método
m = a.reshape([2, 5])
print(m)

# crear un array y sumarle un número
a = np.arange(1, 11)
print(a)
a = a + 5
print(a)

# multiplicarlo por un número
a = a * 2
print(a)

# elevarlo al cuadrado
a = a ** 2
print(a)

#creamos dos arrays
arr1 = np.arange(0, 11)
arr2 = np.arange(20, 31)
print(arr1)
print(arr2)

#los sumamos
arr3 = arr1 + arr2
print(arr3)

#multiplicamos
arr3 = arr1 * arr2
print(arr3)

# Comparaciones
# >,<
arr3 = arr1 > arr2
print(arr3, "\n\n\n")

# pandas
# Importamos pandas
import pandas as pd

# Dataframe -> una estructura de datos tabular que se compone de columnas y filas ordenadas. 

name_age = {"Name" : ["Ali", "Bill", "David", "Hany", "Ibtisam"],
            "Age" : [32, 55, 20, 43, 30]
           }
data_frame = pd.DataFrame(name_age)
print(data_frame)

# Cambiar el orden de las columnas
data_frame_2 = pd.DataFrame(name_age, columns = ['Age', 'Name'])
print(data_frame_2)

# Se pueden generar alias para los nombres de nuestras filas
data_frame_2 = pd.DataFrame(name_age, columns = ['Name', 'Age'], index = ['a', 'b', 'c', 'd', 'e'])
print(data_frame_2)

# Series ->  objeto unidimensional (1D) similar a la columna de una tabla.
nombres = ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam']
series = pd.Series(nombres, index=[1,2,3,4,5])
print(series)
print(type(series))

# Head y Tail

series = pd.Series(np.random.randn(20000))
print(series.head())
print(series.tail())

# Add
dict_1 = {'A' : [5, 8, 10, 3, 9],'B' : [6, 1, 4, 8, 7]}
dict_2 = {'A' : [4, 3, 7, 6, 1],'B' : [9, 10, 10, 1, 2]}
data_frame_1 = pd.DataFrame(dict_1)
data_frame_2 = pd.DataFrame(dict_2)
data_frame_3 = data_frame_1.add(data_frame_2)
print(data_frame_1)
print(data_frame_2)
print(data_frame_3)

alumnos1 = {"nombre": ["Cristian", "Benito", "Laura"],
           "edad": [35,29,19]}
df1 = pd.DataFrame(alumnos1)

alumnos2 = {"nombre": ["Carlos", "Jose", "Sara"],
           "edad": [32,19,23]}
df2 = pd.DataFrame(alumnos2)

df3 = df1.add(df2)
print(df3)

df4 = df1.append(df2, ignore_index=True)
print(df4)

# Carga del csv

d = pd.read_csv('05_03_weather.csv')
print(d)
print(len(d))
print(d.index)
print(d.columns)
print(d.values)

# Info general
print(d.info())

# Head y Tail

print(d.head()) # Primeras 5 filas
print(d.head(10)) # Primeras 10 filas
print(d.tail()) # Ultimas 5 filas
print(d.tail(10)) # Ultimas 10 filas

# Hacer slicing al dataframe, obtener 10 filas ubicadas entre las filas 20 y 30
print(d[20:31])

# Acceder a una columna en particular del dataframe
print(d['Humidity'].head(10)) 

#### Minimo, maximo y promedio de una columna

print(d['Humidity'].min())
print(d['Humidity'].max())
print(d['Humidity'].mean())

#### Ordenación y selección de series

temps = d['Temperature (C)']
print(type(temps)) # Como se ve, temps es una serie de panda
temps_ordenadas = temps.sort_values(ascending=False)
print(temps_ordenadas[:10])

# Condicionales simples: df["columna"]["condicion"]
media_humedad = d["Humidity"].mean()
print("Media de la humedad:", media_humedad)
condicion = d["Humidity"] <= media_humedad
d["Humidity"][condicion]

# Mostrar una columna diferente, de la que se usa para evaluar la condicion
d["Temperature (C)"][d["Humidity"] <= media_humedad]

# Mostraremos todo el dataframe (todas las columnas) que cumplan una condición
# df[condicion]
d[d["Humidity"] <= media_humedad]

# Mostraremos todo el dataframe (todas las columnas) que cumplan una condición
# d[condicion]
d[d["Summary"] == "Foggy"] # Si queremos evaluar si es dintinto: !=

# Condición multiple con AND (&) 
# &: and (Y lógico)
# |: or (O lógico)
d[ (d["Summary"] == "Foggy") & (d["Precip Type"] == "snow") ] 

# Condición multiple con OR (|)
# &: and (Y lógico)
# |: or (O lógico)
d[ (d["Summary"] == "Foggy") | (d["Precip Type"] == "snow") ] 

# Aplicar un condicional y guardar el resultado en un nuevo dataframe
df2 = d[ (d["Summary"] == "Foggy") & (d["Precip Type"] == "snow") ] 
df2

df2.info()

# Estructura de loc: df.loc[condicion, [columna1, column2, columna3]]
d.loc[ d["Humidity"] <= media_humedad, ["Humidity", "Temperature (C)"] ]

# Alternativa de sintaxis al bloque anterior
condicion = d["Humidity"] <= media_humedad
lista_columnas = ["Humidity", "Temperature (C)"]
d.loc[ condicion, lista_columnas ]

# Mostrar todas las columnas (:) que cumplan la condición
d.loc[ d["Humidity"] <= media_humedad, : ]

### iloc: Herramienta muy similar a loc

d.iloc[0] # Primera fila

d.iloc[:, 0] # Primera columna

d.iloc[0:5] # Primeras cinco filas
# Esto seria igual que con el loc

d.iloc[:, 0:5] # Primeras cinco columnas

d.iloc[[0,2,1]]  # Primera, tercera y segunda filas

d.iloc[:, [0,2,1]]  # Primera, tercera y segunda columnas

# Vamos a agrupar por el Summary
grouped_df = d.groupby("Summary")
print(type(grouped_df))

grouped_df

# Mostrarnos el primer registro de cada grupo
grouped_df.first()

print("Número de grupos: ",len(grouped_df))

# Veamos las categorias y sus coincidencias
print(grouped_df.size())

# Preguntemos por una categoria
grouped_df.get_group("Light Rain")

# Preguntemos por una categoria
grouped_df.get_group("Light Rain")["Humidity"].mean()

d.groupby("Summary").mean()

### Conversión

temps = d['Temperature (C)']
print(type(temps)) # Como se ve, temps es una serie de panda

temps_list = d['Temperature (C)'].tolist() 
print(type(temps_list))

print("\nListado de temperaturas")
for t in temps_list:
    print(round(t, 3))

# Exportación
    
df_ordenado = d.sort_values(by=["Temperature (C)"], ascending=False)
df_final = df_ordenado.iloc[0:100, 0:5] # Primeras 100 filas y primeras 5 columnas
print(df_final)

print(df_final.info())

# Exportación a CSV

ruta_csv = r"./EXPORT_weather.csv" # r = raw
df_final.to_csv(ruta_csv, index = False, header = True, sep = ",")

# Exportación a Excel

ruta_excel = r"./EXPORT_weather.xlsx"
df_final.to_excel(ruta_excel, index = False, header = True, sheet_name='Tiempo')

# Exportación a JSON

ruta_json = r"./EXPORT_weather.json"
df_final.to_json(ruta_json, orient="columns")

# Exportación a HTML

ruta_html = r"./EXPORT_weather.html"
df_final.to_html(ruta_html, index = False)