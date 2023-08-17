from tkinter import Button, Entry, Frame, Label, Menu, StringVar, Tk, simpledialog, messagebox
from ConexionesBBDD import *
from aplicacionGraficaPOO import *

def insertarUser(*args):
    conexion=conectarBBDD("localhost","app-vontade","root","")
    cursor=conexion.cursor()

    #cursor.execute("INSERT INTO USERS_APLICACION VALUES( null, '" + self.miNick.get() + "','" + self.miPwd.get() + "', '" + self.miTUser.get() + "', '" + self.miNombre.get() + "','" + self.miCorreo.get() + "')")
    datos=self.miNick.get(), self.miPwd.get(), self.miTUser.get(), self.miNombre.get(), self.miCorreo.get() 
    sql="INSERT INTO USERS_APLICACION (NICK, PWD, TIPO_USER, NOMBRE, CORREO) VALUES(%s, %s, %s, %s, %s)"
    cursor.execute(sql, (datos))
    conexion.commit()

    messagebox.showinfo("Nuevo usuario", "Registro insertado correctamente")

    cursor.close()
    conexion.close()
    self.actualizarDatos()
    self.limpiarCampos()
    self.borrar_widgets()

def leerUserPorID(self):
    idABuscar=simpledialog.askstring("¿?","Que usuario quieres buscar? (ID)")
    
    conexion=conectarBBDD("localhost","app-vontade","root","")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM USERS_APLICACION WHERE ID_USER_APLICACION=" + idABuscar)
    datosUser=cursor.fetchall()
    self.crear_widgets()
    for u in datosUser:
        self.miId.set(u[0])
        self.miNick.set(u[1])
        self.miPwd.set(u[2])
        self.miTUser.set(u[3])
        self.miNombre.set(u[4])
        self.miCorreo.set(u[5])

    cursor.close()
    conexion.close()

def modificarUser(self):
    conexion=conectarBBDD("localhost","app-vontade","root","")
    cursor=conexion.cursor()

    #cursor.execute("UPDATE USERS_APLICACION SET nick='" + miNick.get() + "', pwd='" + miPwd.get() + "', tipo_user='" + miTUser.get() + "', nombre='" + miNombre.get() + "', correo='" + miCorreo.get() + "' WHERE ID_USER_APLICACION='" + miId.get() + "'")
    datos=self.miNick.get(), self.miPwd.get(), self.miTUser.get(), self.miNombre.get(), self.miCorreo.get() 
    cursor.execute("UPDATE USERS_APLICACION SET nick=%s, pwd=%s, tipo_user=%s, nombre=%s, correo=%s WHERE ID_USER_APLICACION='" + self.miId.get(), (datos))
    conexion.commit()

    messagebox.showinfo("Modificar usuario", "Registro modificado correctamente")

    cursor.close()
    conexion.close()

def borrarUser(self):
    conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")
    cursor=conexion.cursor()

    cursor.execute("DELETE FROM USERS_APLICACION WHERE ID_USER_APLICACION='" + self.miId.get() + "'")
    conexion.commit()

    messagebox.showinfo("Borrar usuario", "Registro borrado correctamente")

    cursor.close()
    conexion.close()
