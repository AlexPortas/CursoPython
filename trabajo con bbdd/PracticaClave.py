import sqlite3

conexion=sqlite3.connect("trabajo con bbdd/GestionPedidos")

cursor=conexion.cursor()

cursor.execute('''
            CREATE TABLE PRODUCTOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_ARTICULO VARCHAR(50),
                PRECIO INTEGER,
                SECCION VARCHAR(20)
            )            
''')
productos=[
("Tenis", 100, "Deportes"),
("Pantalón", 58, "Ropa"),
("Reloj", 40, "Joyas")
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?)", productos)

conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")

productos=cursor.fetchall()

print(productos)

cursor.close()

conexion.close()