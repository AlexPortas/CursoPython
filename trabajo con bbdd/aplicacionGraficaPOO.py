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
        self.btnGuardar=ttk.Button(self.frameDatos, text="Crear usuario", style="my.TButton", command=self.add_usuario)
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
        
    def crear_menu(self):
        self.datosMenu=Menu(self.barraMenu, tearoff=0)
        self.datosMenu.add_command(label="Mostrar datos", command=self.actualizarTabla)

        self.borrarMenu=Menu(self.barraMenu, tearoff=0)
        self.borrarMenu.add_command(label="Deseleccionar", command=self.limpiarCampos)

        self.crudMenu=Menu(self.barraMenu, tearoff=0)
        self.crudMenu.add_command(label="Crear usuario", command=lambda:self.crear_widgets(crear=True))
        self.crudMenu.add_command(label="Modificar usuario", command=lambda:self.crear_widgets(modificar=True))
        self.crudMenu.add_command(label="Eliminar usuario", command=lambda:self.crear_widgets(borrar=True))

        self.barraMenu.add_cascade(label="Refrescar", menu=self.datosMenu)
        self.barraMenu.add_cascade(label="Deseleccionar usuario", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="Acciones", menu=self.crudMenu)

    def crear_datos(self):
        conexion=conectarBBDD("localhost","app-vontade","root","")

        cursor=conexion.cursor()

        cursor.execute("SELECT * FROM USERS_APLICACION")

        users=cursor.fetchall()
        for u in users:
            self.tabla.insert("",END,text=u[0], values=(u[1], u[2],u[3]))
        cursor.close()
        conexion.close()

    def actualizarTabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        self.crear_datos()

    def limpiarCampos(self):
        self.miNick.set("")
        self.miPwd.set("")
        self.miTUser.set("")
        self.old_id.set("")
        self.old_nick.set("")
        self.old_pwd.set("")
        self.old_tuser.set("")

    def add_usuario(self):
        conexion=conectarBBDD("localhost","app-vontade","root","")
        cursor=conexion.cursor()
        #cursor.execute("INSERT INTO USERS_APLICACION VALUES (NULL,'"+self.miNick.get()+"','"+self.miPwd.get()+"','"+self.miTUser.get()+"')")
        datos=self.miNick.get(),self.miPwd.get(),self.miTUser.get()
        cursor.execute("INSERT INTO USERS_APLICACION VALUES (NULL,?,?,?)", datos)
        conexion.commit()
        messagebox.showinfo("Nuevo usuario", "Has introducido un usuario")
        cursor.close()
        conexion.close()
        self.limpiarCampos()
        self.actualizarTabla()

    def eliminar_usuario(self):
        #Comprobación de que se seleccione un producto para eliminarlo
        try:
            self.tabla.item(self.tabla.selection())["text"]
        except IndexError as e:
            messagebox.showerror("Sin datos", "Por favor, seleccione un usuario")
            return

        self.old_id.set(self.tabla.item(self.tabla.selection())['text'])
        self.miNick.set(self.tabla.item(self.tabla.selection())['values'][0])
        self.miPwd.set(self.tabla.item(self.tabla.selection())['values'][1])
        self.miTUser.set(self.tabla.item(self.tabla.selection())['values'][2])
                
        #Ventana nueva eliminar usuario
        self.ventana_eliminar = Toplevel()  # Crear una ventana por delante de la principal
        self.ventana_eliminar.title("Eliminar Usuario")  # Titulo de la ventana
        self.ventana_eliminar.resizable(1, 1)

        titulo = Label(self.ventana_eliminar, text='¿Quieres eliminar a?', font=('Calibri', 50, 'bold'))
        titulo.grid(column=0, row=0, columnspan=2)

        self.etiqueta_nick = ttk.Label(self.ventana_eliminar, text = "Nick: ", font=('Calibri', 13))
        self.etiqueta_nick.grid(row=2, column=0)
        self.input_nick = ttk.Entry(self.ventana_eliminar, textvariable=self.miNick, state='readonly', font=('Calibri', 13))
        self.input_nick.grid(row=2, column=1)
                
        self.etiqueta_pwd = ttk.Label(self.ventana_eliminar, text="Contraseña: ", font=('Calibri', 13))
        self.etiqueta_pwd.grid(row=3, column=0)
        self.input_pwd = ttk.Entry(self.ventana_eliminar, textvariable=self.miPwd, state='readonly', font=('Calibri', 13))
        self.input_pwd.grid(row=3, column=1)
        
        self.etiqueta_tuser = ttk.Label(self.ventana_eliminar, text="Tipo: ", font=('Calibri', 13))
        self.etiqueta_tuser.grid(row=4, column=0)
        self.input_tuser = ttk.Entry(self.ventana_eliminar, textvariable=self.miTUser, state='readonly', font=('Calibri', 13))
        self.input_tuser.grid(row=4, column=1)
    
        # Boton Actualizar Producto
        s = ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))
        self.boton_eliminar = ttk.Button(self.ventana_eliminar, text="Eliminar", style="my.TButton", command=self.delete_usuario)
        self.boton_eliminar.grid(row=5, column=0, sticky=W + E)
        self.btnEditar=ttk.Button(self.ventana_eliminar, text="CANCELAR", style="my.TButton", command=lambda:self.volver_usuario(self.ventana_eliminar))
        self.btnEditar.grid(row=5, column=1, sticky=W+E)

    def delete_usuario(self):        
        conexion=conectarBBDD("localhost","app-vontade","root","")
        cursor=conexion.cursor()
        cursor.execute("DELETE FROM USERS_APLICACION WHERE ID='"+self.old_id.get()+"'")
        conexion.commit()
        messagebox.showinfo("Eliminar usuario", "Has eliminado un usuario")
        cursor.close()
        conexion.close()
        self.limpiarCampos()
        self.actualizarTabla()

    def editar_usuario(self):
        #Comprobación de que se seleccione un producto para editarlo
        try:
            self.tabla.item(self.tabla.selection())["text"]
        except IndexError as e:
            messagebox.showerror("Sin datos", "Por favor, seleccione un usuario")
            return
        
        self.old_id.set(self.tabla.item(self.tabla.selection())['text'])
        self.old_nick.set(self.tabla.item(self.tabla.selection())['values'][0])
        self.old_pwd.set(self.tabla.item(self.tabla.selection())['values'][1])
        self.old_tuser.set(self.tabla.item(self.tabla.selection())['values'][2])
        #Ventana nueva (editar usuario
        self.ventana_editar = Toplevel()  # Crear una ventana por delante de la principal
        self.ventana_editar.title("Editar Usuario")  # Titulo de la ventana
        self.ventana_editar.resizable(1, 1)

        titulo = Label(self.ventana_editar, text='Edición de Usuario', font=('Calibri', 50, 'bold'))
        titulo.grid(column=0, row=0, columnspan=2)

        self.etiqueta_nick_anituguo = ttk.Label(self.ventana_editar, text = "Nick antiguo: ", font=('Calibri', 13))
        self.etiqueta_nick_anituguo.grid(row=2, column=0)
        self.input_nick_antiguo = ttk.Entry(self.ventana_editar, textvariable=self.old_nick, state='readonly', font=('Calibri', 13))
        self.input_nick_antiguo.grid(row=2, column=1)
        
        self.etiqueta_nick_nuevo = ttk.Label(self.ventana_editar, text="Nick nuevo: ", font=('Calibri', 13))
        self.etiqueta_nick_nuevo.grid(row=3, column=0)
        self.input_nick_nuevo = ttk.Entry(self.ventana_editar, font=('Calibri', 13))
        self.input_nick_nuevo.grid(row=3, column=1)
        
        self.etiqueta_pwd_anituguo = ttk.Label(self.ventana_editar, text="Contraseña antiguo: ", font=('Calibri', 13))
        self.etiqueta_pwd_anituguo.grid(row=4, column=0)
        self.input_pwd_antiguo = ttk.Entry(self.ventana_editar, textvariable=self.old_pwd, state='readonly', font=('Calibri', 13))
        self.input_pwd_antiguo.grid(row=4, column=1)
        
        self.etiqueta_pwd_nuevo = ttk.Label(self.ventana_editar, text="Contraseña nuevo: ", font=('Calibri', 13))
        self.etiqueta_pwd_nuevo.grid(row=5, column=0)
        self.input_pwd_nuevo = ttk.Entry(self.ventana_editar, font=('Calibri', 13))
        self.input_pwd_nuevo.grid(row=5, column=1)
        
        self.etiqueta_tuser_anituguo = ttk.Label(self.ventana_editar, text="Tipo antiguo: ", font=('Calibri', 13))
        self.etiqueta_tuser_anituguo.grid(row=6, column=0)
        self.input_tuser_antiguo = ttk.Entry(self.ventana_editar, textvariable=self.old_tuser, state='readonly', font=('Calibri', 13))
        self.input_tuser_antiguo.grid(row=6, column=1)
        
        self.etiqueta_tuser_nuevo = ttk.Label(self.ventana_editar, text="Tipo nuevo: ", font=('Calibri', 13))
        self.etiqueta_tuser_nuevo.grid(row=7, column=0)
        self.input_tuser_nuevo = ttk.Entry(self.ventana_editar, font=('Calibri', 13))
        self.input_tuser_nuevo.grid(row=7, column=1)
    
        # Boton Actualizar Producto
        s = ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))
        self.boton_actualizar = ttk.Button(self.ventana_editar, text="Actualizar", style="my.TButton", command=lambda: self.actualizar_usuario(self.input_nick_nuevo.get(), self.input_pwd_nuevo.get(), self.input_tuser_nuevo.get(), self.old_id.get()))
        self.boton_actualizar.grid(row=8, column=0, sticky=W + E)
        self.btnEditar=ttk.Button(self.ventana_editar, text="CANCELAR", style="my.TButton", command=lambda:self.volver_usuario(self.ventana_editar))
        self.btnEditar.grid(row=8, column=1, sticky=W+E)

    def actualizar_usuario(self, nick, pwd, tuser, id):
        conexion=conectarBBDD("localhost","app-vontade","root","")
        cursor=conexion.cursor()
       # cursor.execute("UPDATE USERS_APLICACION SET nick='"+nick+"', pwd='"+pwd+"',tipo='"+tuser+"' WHERE ID='"+id+"'")
        datos=nick, pwd, tuser, id
        cursor.execute("UPDATE USERS_APLICACION SET nick=?, pwd=?,tipo=? WHERE ID=?",datos)
        conexion.commit()
        messagebox.showinfo("Actualizastes usuario", "Has actualizado un usuario")
        cursor.close()
        conexion.close()
        self.ventana_editar.destroy()
        self.limpiarCampos()
        self.actualizarTabla()
      
    def volver_usuario(self, frame):
        frame.destroy()
        self.limpiarCampos()

root=Tk()
app=CrudPOO(root)
app.mainloop()