import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect("ejemplo.db")

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()

# Insertando un registro

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# Insertamos un registro en la tabla de usuarios
cursor.execute("INSERT INTO usuarios VALUES ('Cristian', 30, 'cristian@pruebas.es')")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()

# Recuperando el primer registro con .fetchone()

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Recorremos el primer registro con el método fetchone, devuelve una tupla
usuario = cursor.fetchone()
print(usuario)

conexion.close()

# Recuperando varios registros con .fetchall()

conexion = sqlite3.connect('ejemplo.db')
cursor = conexion.cursor()

# Recuperamos los registros de la tabla de usuarios
cursor.execute("SELECT * FROM usuarios")

# Recorremos todos los registros con fetchall, y los volvamos en una lista de usuarios
usuarios = cursor.fetchall()

# Ahora podemos recorrer todos los usuarios
for usuario in usuarios:
    print(usuario)

conexion.close()