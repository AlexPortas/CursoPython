import tkinter
import mysql.connector
from tkinter import *

# ----------------- conexion bbdd ---------------------------
conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")

cursor=conexion.cursor()

#cursor.execute("INSERT INTO USERS_APLICACION VALUES( null, 'Alex','PASSWORD', 2, 'Prueba', 'info@gmail.com')")

#conexion.commit()

cursor.execute("SELECT * FROM USERS_APLICACION")

productos=cursor.fetchall()

print(productos)

cursor.close()

# ------------------ Aplicación gráfica -----------------------------------

raiz=Tk()

frame=Frame(raiz, width=1000, height=700)

frame.pack()

cuadroTextoNick=Entry(frame).grid(row=0, column=1, padx=15, pady=15)

nickLabel=Label(frame, text="Nick: ").grid(row=0, column=0, sticky="w", padx=10)

cuadroTextoPwd=Entry(frame).grid(row=1, column=1, padx=15, pady=15)

contraseñaLabel=Label(frame, text="Contraseña: ").grid(row=1, column=0, sticky="w", padx=10)

cuadroTextoTUser=Entry(frame).grid(row=2, column=1, padx=15, pady=15)

tipoUserLabel=Label(frame, text="Tipo usuario: ").grid(row=2, column=0, sticky="w", padx=10)

cuadroTextoNombre=Entry(frame).grid(row=3, column=1, padx=15, pady=15)

nombreLabel=Label(frame, text="Nombre: ").grid(row=3, column=0, sticky="w", padx=10)

cuadroTextoCorreo=Entry(frame).grid(row=4, column=1, padx=15, pady=15)

correoLabel=Label(frame, text="Dirección electronica: ").grid(row=4, column=0, sticky="w", padx=10)


def funcionClick():
    tkinter.messagebox.showinfo("Saludo", "Hola " + cuadroTextoNombre.get())

btnEnviar=Button(raiz, text="Enviar", command=funcionClick)

btnEnviar.pack()

raiz.mainloop()