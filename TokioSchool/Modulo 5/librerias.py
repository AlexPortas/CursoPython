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
print(arr3)

# ==
arr3 = arr1 == arr2 # ¡ojo! los arrays son de integers, no de floats
print(arr3)