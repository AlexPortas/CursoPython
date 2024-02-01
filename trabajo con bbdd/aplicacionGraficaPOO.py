from tkinter import Button, Entry, Frame, Label, Menu, StringVar, Tk
from ConexionesBBDD import *
from FuncionesCRUD import *

class CrudPOO(Frame):
    def __init__(self, raiz):
        # ----- Config ventana
        self.ventana = raiz
        self.ventana.title("App Gestor de Usuarips de la aplicacióm")
        self.ventana.resizable(1,1)
        self.ventana.wm_iconbitmap("recursos/logo.ico")
        
        # ----- Variables de control
        self.miId=StringVar()  
        self.miNick=StringVar()
        self.miPwd=StringVar()
        self.miTUser=StringVar()
        self.miNombre=StringVar()
        self.miCorreo=StringVar()

        #------------- barra de menu

        self.barraMenu=Menu(self.ventana)
        raiz.config(menu=self.barraMenu)

        super().__init__(self.ventana)
        self.master=raiz
        self.pack()
        
        self.frameDatos=Frame(self.ventana)
        self.frameDatos.pack()   

        self.tabla=ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.tabla.grid(row=4, columnspan=2)
        self.tabla.heading("#0", text="ID", anchor=CENTER)
        self.tabla.heading("#1", text="Nombre", anchor=CENTER)
        self.tabla.heading("#2", text="Contraseña", anchor=CENTER)
        self.tabla.heading("#3", text="Tipo", anchor=CENTER)
        
        self.crear_datos()
        self.crear_menu()
        
    def crear_menu(self):
        self.datosMenu=Menu(self.barraMenu, tearoff=0)
        self.datosMenu.add_command(label="Mostrar datos", command=self.actualizarDatos)

        self.borrarMenu=Menu(self.barraMenu, tearoff=0)
        self.borrarMenu.add_command(label="Desseleccionar", command=self.limpiarCampos)

        self.crudMenu=Menu(self.barraMenu, tearoff=0)
        self.crudMenu.add_command(label="Crear usuario", command=lambda:self.crear_widgets(crear=True))
        self.crudMenu.add_command(label="Leer usuario por Id", command=lambda:self.crear_widgets(mostrar=True))
        self.crudMenu.add_command(label="Modificar usuario", command=lambda:self.crear_widgets(modificar=True))
        self.crudMenu.add_command(label="Eliminar usuario", command=lambda:self.crear_widgets(borrar=True))

        self.barraMenu.add_cascade(label="Refrescar", menu=self.datosMenu)
        self.barraMenu.add_cascade(label="Desseleccionar usuario", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="Acciones", menu=self.crudMenu)

    def crear_widgets(self, crear=False, mostrar=False, modificar=False, borrar=False):
        self.borrar_widgets()
        if not crear:
            self.cuadroTextoId=Entry(self, textvariable=self.miId).grid(row=0, column=2, padx=5, pady=5)
            self.idLabel=Label(self, text="Id: ").grid(row=0, column=1, sticky="w", padx=10)

        self.cuadroTextoNick=Entry(self, textvariable=self.miNick).grid(row=1, column=2, padx=5, pady=5)
        self.nickLabel=Label(self, text="Nick: ").grid(row=1, column=1, sticky="w", padx=10)

        self.cuadroTextoPwd=Entry(self, textvariable=self.miPwd).grid(row=2, column=2, padx=5, pady=5)
        self.contraseñaLabel=Label(self, text="Contraseña: ").grid(row=2, column=1, sticky="w", padx=10)

        self.cuadroTextoTUser=Entry(self, textvariable=self.miTUser).grid(row=3, column=2, padx=5, pady=5)
        self.tipoUserLabel=Label(self, text="Tipo usuario: ").grid(row=3, column=1, sticky="w", padx=10)

        self.cuadroTextoNombre=Entry(self, textvariable=self.miNombre).grid(row=4, column=2, padx=5, pady=5)
        self.nombreLabel=Label(self, text="Nombre: ").grid(row=4, column=1, sticky="w", padx=10)

        self.cuadroTextoCorreo=Entry(self, textvariable=self.miCorreo).grid(row=5, column=2, padx=5, pady=5)
        self.correoLabel=Label(self, text="Dirección electronica: ").grid(row=5, column=1, sticky="w", padx=10)

        if crear:
            self.btnCrear=Button(self, text="Crear usuario", command=self.insertarUser).grid(row=6, column=2)

        if mostrar:
            self.leerUserPorID()
            self.btnMostrar=Button(self, text="Mostrar otro usuario", command=self.leerUserPorID).grid(row=6, column=2)

        if modificar:
            self.btnCrear=Button(self, text="Modificar usuario", command=self.modificarUser).grid(row=6, column=2)

        if borrar:
            self.btnCrear=Button(self, text="Borrar usuario", command=self.borrarUser).grid(row=6, column=2)

    def crear_datos(self):
        self.idLabel=Label(self.frameDatos, text="Id").grid(row=0, column=0, sticky="w", padx=10)
        self.nickLabel=Label(self.frameDatos, text="Nick").grid(row=0, column=1, sticky="w", padx=10)
        self.contraseñaLabel=Label(self.frameDatos, text="Contraseña").grid(row=0, column=2, sticky="w", padx=10)
        self.tipoUserLabel=Label(self.frameDatos, text="Tipo usuario").grid(row=0, column=3, sticky="w", padx=10)
        conexion=conectarBBDD("localhost","app-vontade","root","")

        cursor=conexion.cursor()

        cursor.execute("SELECT * FROM USERS_APLICACION")

        users=cursor.fetchall()
        cont=1
        for u in users:
            Label(self.frameDatos, text=u[0]).grid(row=cont, column=0, sticky="w", padx=10)
            Label(self.frameDatos, text=u[1]).grid(row=cont, column=1, sticky="w", padx=10)
            Label(self.frameDatos, text=u[2]).grid(row=cont, column=2, sticky="w", padx=10)
            Label(self.frameDatos, text=u[3]).grid(row=cont, column=3, sticky="w", padx=10)
            cont+=1
        Label(self.frameDatos).grid(row=cont,pady=1)
        cursor.close()
        conexion.close()

    def actualizarDatos(self):
        for widget in self.frameDatos.winfo_children():
            widget.destroy()
        self.crear_datos()

    def borrar_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.grid_forget()

    def limpiarCampos(self):
        self.miId.set("")
        self.miNick.set("")
        self.miPwd.set("")
        self.miTUser.set("")
        self.miNombre.set("")
        self.miCorreo.set("")


root=Tk()
app=CrudPOO(root)
app.mainloop()