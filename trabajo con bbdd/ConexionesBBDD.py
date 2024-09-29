from tkinter import END, Text
import mysql.connector

def conectarBBDD(host, db, user, pwd):
    return mysql.connector.connect(host=host, database=db, user=user, password=pwd)

def limpiarCampos(*args):
    for campo in args:
        if type(campo)==Text:
            campo.delete(1.0, END)
        else:
            campo.set("")



def crear_datos(tabla):
    conexion=conectarBBDD("localhost","app-vontade","root","")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM USERS_APLICACION")
    users=cursor.fetchall() 
    for u in users:
        tabla.insert("",END,text=u[0], values=(u[1], u[2],u[3]))
    cursor.close()
    conexion.close()

def actualizarTabla(tabla):
    for fila in tabla.get_children():
        tabla.delete(fila)
    crear_datos(tabla)

def db_consulta(conexion, query, parametros=()):
    with conexion as con:
        cursor=con.cursor()
        resultado=cursor.execute(query, parametros)
        con.commit()
    return resultado