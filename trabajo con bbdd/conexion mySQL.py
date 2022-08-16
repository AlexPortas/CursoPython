import mysql.connector

conexion=mysql.connector.connect(host="localhost", database="prueba", user="root", password="")

cursor=conexion.cursor()

cursor.execute("INSERT INTO ALUMNOS VALUES( null, 'Alex','Alonso', 44)")

conexion.commit()

cursor.execute("SELECT * FROM ALUMNOS")

productos=cursor.fetchall()

print(productos)

cursor.close()
