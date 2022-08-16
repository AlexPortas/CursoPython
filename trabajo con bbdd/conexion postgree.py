import psycopg2

conexion=psycopg2.connect(host="localhost", database="Personas", user="postgres", password="root")

cursor=conexion.cursor()

#cursor.execute("CREATE TABLE PRODUCTOS (ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
cursor.execute(" INSERT INTO ALUMNOS VALUES('Alex','Alonso')")

conexion.commit()

cursor.execute("SELECT * FROM ALUMNOS")

productos=cursor.fetchall()

print(productos)

cursor.close()
