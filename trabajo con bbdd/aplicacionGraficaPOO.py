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
        self.miNick=StringVar()
        self.miPwd=StringVar()
        self.miTUser=StringVar()
        self.old_id=StringVar()
        self.old_nick=StringVar()
        self.old_pwd=StringVar()
        self.old_tuser=StringVar()

        #------------- barra de menu

        self.barraMenu=Menu(self.ventana)
        raiz.config(menu=self.barraMenu)

        super().__init__(self.ventana)
        self.master=raiz
        self.grid(row=0)
        
        self.frameDatos=LabelFrame(self.ventana, text="Registrar nuevo usuario", font=('Calibri', 16, 'bold'))
        self.frameDatos.grid(row=0, column=0, columnspan=4, pady=20)

        self.cuadroTextoNick=ttk.Entry(self.frameDatos, textvariable=self.miNick)
        self.cuadroTextoNick.grid(row=1, column=2, padx=5, pady=5)
        self.nickLabel=ttk.Label(self.frameDatos, text="Nick: ")
        self.nickLabel.grid(row=1, column=1, sticky="w", padx=10)

        self.cuadroTextoPwd=ttk.Entry(self.frameDatos, textvariable=self.miPwd)
        self.cuadroTextoPwd.grid(row=2, column=2, padx=5, pady=5)
        self.contraseñaLabel=ttk.Label(self.frameDatos, text="Contraseña: ")
        self.contraseñaLabel.grid(row=2, column=1, sticky="w", padx=10)

        self.cuadroTextoTUser=ttk.Entry(self.frameDatos, textvariable=self.miTUser)
        self.cuadroTextoTUser.grid(row=3, column=2, padx=5, pady=5)
        self.tipoUserLabel=ttk.Label(self.frameDatos, text="Tipo usuario: ")
        self.tipoUserLabel.grid(row=3, column=1, sticky="w", padx=10)

        s = ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))
        self.btnGuardar=ttk.Button(self.frameDatos, text="Crear usuario", style="my.TButton", command=add_usuario)
        self.btnGuardar.grid(row=4, column=1, columnspan=2, sticky=W+E)

        #crear tabla
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
        

        #botones eliminar y editar
        s=ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))

        self.btnEliminar=ttk.Button(text="ELIMINAR", style="my.TButton", command=self.eliminar_usuario)
        self.btnEliminar.grid(row=5, column=0, sticky=W+E)
        self.btnEditar=ttk.Button(text="EDITAR", style="my.TButton", command=self.editar_usuario)
        self.btnEditar.grid(row=5, column=1, sticky=W+E)

        self.crear_datos()
        self.crear_menu()
        
root=Tk()
app=CrudPOO(root)
app.mainloop()