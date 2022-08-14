import sqlite3

conexion=sqlite3.connect("trabajo con bbdd/db")

cursor=conexion.cursor()

#cursor.execute("CREATE TABLE PRODUCTOS (ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
cursor.execute(" INSERT INTO PRODUCTOS VALUES('Camiseta',15,'Ropa')")

conexion.commit()

cursor.close()

conexion.close()