import sqlite3

conexion=sqlite3.connect("trabajo con bbdd/db")

cursor=conexion.cursor()

#cursor.execute("CREATE TABLE PRODUCTOS (ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#cursor.execute(" INSERT INTO PRODUCTOS VALUES('Camiseta',15,'Ropa')")
'''productos=[
("Tenis", 100, "Deportes"),
("Pantalón", 58, "Ropa"),
("Reloj", 40, "Joyas")
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?)", productos)'''

cursor.execute("SELECT * FROM PRODUCTOS")

productos=cursor.fetchall()

print(productos)
#conexion.commit()

cursor.close()

conexion.close()