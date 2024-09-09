from tkinter import *
from tkinter import ttk
from ConexionesBBDD import *
from FuncionesCRUD import *

class CrudPOO(Frame):
    def __init__(self, raiz):
        # ----- Config ventana
        self.ventana = raiz
        self.ventana.title("App Gestor de Usuarips de la aplicacióm")
        self.ventana.resizable(1,1)
        
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
        self.grid(row=0)
        
        self.frameDatos=LabelFrame(self.ventana, text="Registrar nuevo usuario", font=('Calibri', 16, 'bold'))
        self.frameDatos.grid(row=0, column=0, columnspan=4, pady=20)
        self.crear_widgets(self.frameDatos )
        self.tabla=ttk.Treeview(height=20, columns=("Nombre","Contraseña","Tipo"), style="mystyle.Treeview")
        self.tabla.grid(row=4, columnspan=2)
        self.tabla.column("#0", width=80, anchor=CENTER)
        self.tabla.column("Nombre", width=80, anchor=CENTER)
        self.tabla.column("Contraseña", width=80, anchor=CENTER)
        self.tabla.column("Tipo", width=80, anchor=CENTER)
        self.tabla.heading("#0", text="ID", anchor=CENTER)
        self.tabla.heading("Nombre", text="Nombre", anchor=CENTER)
        self.tabla.heading("Contraseña", text="Contraseña", anchor=CENTER)
        self.tabla.heading("Tipo", text="Tipo", anchor=CENTER)
        
        self.crear_datos()
        self.crear_menu()
        
    def crear_menu(self):
        self.datosMenu=Menu(self.barraMenu, tearoff=0)
        self.datosMenu.add_command(label="Mostrar datos", command=self.actualizarDatos)

        self.borrarMenu=Menu(self.barraMenu, tearoff=0)
        self.borrarMenu.add_command(label="Deseleccionar", command=self.limpiarCampos)

        self.crudMenu=Menu(self.barraMenu, tearoff=0)
        self.crudMenu.add_command(label="Crear usuario", command=lambda:self.crear_widgets(crear=True))
        self.crudMenu.add_command(label="Leer usuario por Id", command=lambda:self.crear_widgets(mostrar=True))
        self.crudMenu.add_command(label="Modificar usuario", command=lambda:self.crear_widgets(modificar=True))
        self.crudMenu.add_command(label="Eliminar usuario", command=lambda:self.crear_widgets(borrar=True))

        self.barraMenu.add_cascade(label="Refrescar", menu=self.datosMenu)
        self.barraMenu.add_cascade(label="Deseleccionar usuario", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="Acciones", menu=self.crudMenu)

    def crear_widgets(self, frame):
        self.cuadroTextoNick=ttk.Entry(frame, textvariable=self.miNick).grid(row=1, column=2, padx=5, pady=5)
        self.nickLabel=ttk.Label(frame, text="Nick: ").grid(row=1, column=1, sticky="w", padx=10)

        self.cuadroTextoPwd=ttk.Entry(frame, textvariable=self.miPwd).grid(row=2, column=2, padx=5, pady=5)
        self.contraseñaLabel=ttk.Label(frame, text="Contraseña: ").grid(row=2, column=1, sticky="w", padx=10)

        self.cuadroTextoTUser=ttk.Entry(frame, textvariable=self.miTUser).grid(row=3, column=2, padx=5, pady=5)
        self.tipoUserLabel=ttk.Label(frame, text="Tipo usuario: ").grid(row=3, column=1, sticky="w", padx=10)

        s = ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))
        self.btnGuardar=ttk.Button(frame, text="Crear usuario", style="my.TButton")
        self.btnGuardar.grid(row=4, columnspan=2, sticky=W+E)

    def crear_datos(self):
        conexion=conectarBBDD("localhost","app-vontade","root","")

        cursor=conexion.cursor()

        cursor.execute("SELECT * FROM USERS_APLICACION")

        users=cursor.fetchall()
        cont=1
        for u in users:
            self.tabla.insert("",END,text=u[0], values=(u[1], u[2],u[3]))
            cont+=1
        Label(self.frameDatos).grid(row=cont,pady=1)
        cursor.close()
        conexion.close()


    def actualizarDatos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        self.crear_datos()

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