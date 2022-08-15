import sqlite3

conexion=sqlite3.connect("trabajo con bbdd/GestionPedidos")

cursor=conexion.cursor()

productos=[
("Tenis", 100, "Deportes"),
("Pantalón", 58, "Ropa"),
("Reloj", 40, "Joyas")
]

cursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE ID=3")

conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")

productos=cursor.fetchall()

print(productos)

cursor.execute("DELETE FROM PRODUCTOS WHERE ID=2")

conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")

productos=cursor.fetchall()

print(productos)

cursor.close()

conexion.close()