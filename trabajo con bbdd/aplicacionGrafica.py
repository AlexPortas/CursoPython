from tkinter import messagebox
import mysql.connector
from tkinter import *
# ------------------ Aplicación gráfica -----------------------------------

raiz=Tk()

raiz.title("Gestion usuarios aplicación")

#raiz.geometry("700x350")

# ---------------------------------- Funciones --------------------------------
def refrescar():
    for widget in frameDatos.winfo_children():
        widget.destroy()
    idLabel=Label(frameDatos, text="Id").grid(row=0, column=0, sticky="w", padx=10)
    nickLabel=Label(frameDatos, text="Nick").grid(row=0, column=1, sticky="w", padx=10)
    contraseñaLabel=Label(frameDatos, text="Contraseña").grid(row=0, column=2, sticky="w", padx=10)
    tipoUserLabel=Label(frameDatos, text="Tipo usuario").grid(row=0, column=3, sticky="w", padx=10)
    nombreLabel=Label(frameDatos, text="Nombre").grid(row=0, column=4, sticky="w", padx=10)
    correoLabel=Label(frameDatos, text="Dirección electronica").grid(row=0, column=5, sticky="w", padx=10)

    conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")

    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM USERS_APLICACION")

    users=cursor.fetchall()
    cont=1
    for u in users:
        idLabel=Label(frameDatos, text=u[0]).grid(row=cont, column=0, sticky="w", padx=10)
        nickLabel=Label(frameDatos, text=u[1]).grid(row=cont, column=1, sticky="w", padx=10)
        contraseñaLabel=Label(frameDatos, text=u[2]).grid(row=cont, column=2, sticky="w", padx=10)
        tipoUserLabel=Label(frameDatos, text=u[3]).grid(row=cont, column=3, sticky="w", padx=10)
        nombreLabel=Label(frameDatos, text=u[4]).grid(row=cont, column=4, sticky="w", padx=10)
        correoLabel=Label(frameDatos, text=u[5]).grid(row=cont, column=5, sticky="w", padx=10)
        cont+=1
    Label(frameDatos).grid(row=cont,pady=10)
    cursor.close()
    conexion.close()
       
def limpiarCampos():
    miId.set("")
    miNick.set("")
    miPwd.set("")
    miTUser.set("")
    miNombre.set("")
    miCorreo.set("")

def insertarUser():
    conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")
    cursor=conexion.cursor()

    cursor.execute("INSERT INTO USERS_APLICACION VALUES( null, '" + miNick.get() + "','" + miPwd.get() + "', '" + miTUser.get() + "', '" + miNombre.get() + "','" + miCorreo.get() + "')")
    #datos=miNick.get(), miPwd.get(), miTUser.get(), miNombre.get(), miCorreo.get() 
    #cursor.execute("INSERT INTO USERS_APLICACION VALUES( null, ?, ?, ?, ?, ?)", (datos))
    conexion.commit()

    messagebox.showinfo("Nuevo usuario", "Registro insertado correctamente")

    cursor.close()
    conexion.close()

def leerUserPorID():
    conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")
    cursor=conexion.cursor()

    cursor.execute("SELECT * FROM USERS_APLICACION WHERE ID_USER_APLICACION=" + miId.get())
    datosUser=cursor.fetchall()
    for u in datosUser:
        miId.set(u[0])
        miNick.set(u[1])
        miPwd.set(u[2])
        miTUser.set(u[3])
        miNombre.set(u[4])
        miCorreo.set(u[5])

    cursor.close()
    conexion.close()


def modificarUser():
    conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")
    cursor=conexion.cursor()

    #cursor.execute("UPDATE USERS_APLICACION SET nick='" + miNick.get() + "', pwd='" + miPwd.get() + "', tipo_user='" + miTUser.get() + "', nombre='" + miNombre.get() + "', correo='" + miCorreo.get() + "' WHERE ID_USER_APLICACION='" + miId.get() + "'")
    datos=miNick.get(), miPwd.get(), miTUser.get(), miNombre.get(), miCorreo.get() 
    cursor.execute("UPDATE USERS_APLICACION SET nick=?, pwd=?, tipo_user=?, nombre=?, correo=? WHERE ID_USER_APLICACION='" + miId.get(), (datos))
    conexion.commit()

    messagebox.showinfo("Modificar usuario", "Registro modificado correctamente")

    cursor.close()
    conexion.close()

def borrarUser():
    conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")
    cursor=conexion.cursor()

    cursor.execute("DELETE FROM USERS_APLICACION WHERE ID_USER_APLICACION='" + miId.get() + "'")
    conexion.commit()

    messagebox.showinfo("Borrar usuario", "Registro borrado correctamente")

    cursor.close()
    conexion.close()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

# ----- Variables de control
miId=StringVar()
miNick=StringVar()
miPwd=StringVar()
miTUser=StringVar()
miNombre=StringVar()
miCorreo=StringVar()


datosMenu=Menu(barraMenu, tearoff=0)
datosMenu.add_command(label="Mostrar datos", command=refrescar)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Desseleccionar", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear usuario", command=insertarUser)
crudMenu.add_command(label="Leer usuario por Id", command=leerUserPorID)
crudMenu.add_command(label="Modificar usuario", command=modificarUser)
crudMenu.add_command(label="Eliminar usuario", command=borrarUser)

barraMenu.add_cascade(label="Refrescar", menu=datosMenu)
barraMenu.add_cascade(label="Desseleccionar usuario", menu=borrarMenu)
barraMenu.add_cascade(label="Acciones", menu=crudMenu)

frameDatos=Frame(raiz)

frameDatos.pack()

idLabel=Label(frameDatos, text="Id").grid(row=0, column=0, sticky="w", padx=10)
nickLabel=Label(frameDatos, text="Nick").grid(row=0, column=1, sticky="w", padx=10)
contraseñaLabel=Label(frameDatos, text="Contraseña").grid(row=0, column=2, sticky="w", padx=10)
tipoUserLabel=Label(frameDatos, text="Tipo usuario").grid(row=0, column=3, sticky="w", padx=10)
nombreLabel=Label(frameDatos, text="Nombre").grid(row=0, column=4, sticky="w", padx=10)
correoLabel=Label(frameDatos, text="Dirección electronica").grid(row=0, column=5, sticky="w", padx=10)

conexion=mysql.connector.connect(host="localhost", database="app-vontade", user="root", password="")

cursor=conexion.cursor()

cursor.execute("SELECT * FROM USERS_APLICACION")

users=cursor.fetchall()
cont=1
for u in users:
    idLabel=Label(frameDatos, text=u[0]).grid(row=cont, column=0, sticky="w", padx=10)
    nickLabel=Label(frameDatos, text=u[1]).grid(row=cont, column=1, sticky="w", padx=10)
    contraseñaLabel=Label(frameDatos, text=u[2]).grid(row=cont, column=2, sticky="w", padx=10)
    tipoUserLabel=Label(frameDatos, text=u[3]).grid(row=cont, column=3, sticky="w", padx=10)
    nombreLabel=Label(frameDatos, text=u[4]).grid(row=cont, column=4, sticky="w", padx=10)
    correoLabel=Label(frameDatos, text=u[5]).grid(row=cont, column=5, sticky="w", padx=10)
    cont+=1
Label(frameDatos).grid(row=cont,pady=10)
cursor.close()
conexion.close()

frame=Frame(raiz)
frame.pack()
cuadroTextoId=Entry(frame, textvariable=miId).grid(row=0, column=1, padx=5, pady=5)
idLabel=Label(frame, text="Id: ").grid(row=0, column=0, sticky="w", padx=10)

cuadroTextoNick=Entry(frame, textvariable=miNick).grid(row=1, column=1, padx=5, pady=5)
nickLabel=Label(frame, text="Nick: ").grid(row=1, column=0, sticky="w", padx=10)

cuadroTextoPwd=Entry(frame, textvariable=miPwd).grid(row=2, column=1, padx=5, pady=5)
contraseñaLabel=Label(frame, text="Contraseña: ").grid(row=2, column=0, sticky="w", padx=10)

cuadroTextoTUser=Entry(frame, textvariable=miTUser).grid(row=3, column=1, padx=5, pady=5)
tipoUserLabel=Label(frame, text="Tipo usuario: ").grid(row=3, column=0, sticky="w", padx=10)

cuadroTextoNombre=Entry(frame, textvariable=miNombre).grid(row=4, column=1, padx=5, pady=5)
nombreLabel=Label(frame, text="Nombre: ").grid(row=4, column=0, sticky="w", padx=10)

cuadroTextoCorreo=Entry(frame, textvariable=miCorreo).grid(row=5, column=1, padx=5, pady=5)
correoLabel=Label(frame, text="Dirección electronica: ").grid(row=5, column=0, sticky="w", padx=10)

Label(frame).grid(row=6,pady=10)

raiz.mainloop()