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

        #------------- barra de menu

        self.barraMenu=Menu(self.ventana)
        raiz.config(menu=self.barraMenu)

        super().__init__(self.ventana)
        self.master=raiz
        self.grid(row=0)
        
        self.frameDatos=LabelFrame(self.ventana, text="Registrar nuevo usuario", font=('Calibri', 16, 'bold'))
        self.frameDatos.grid(row=0, column=0, columnspan=4, pady=20)
        self.crear_widgets(self.frameDatos, 1)
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

        self.btnEliminar=ttk.Button(text="ELIMINAR", style="my.TButton")#, command=self.eliminar_usuario)
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

    def crear_widgets(self, frame, opcion):
        if opcion==1:
            self.cuadroTextoNick=ttk.Entry(frame, textvariable=self.miNick).grid(row=1, column=2, padx=5, pady=5)
            self.nickLabel=ttk.Label(frame, text="Nick: ").grid(row=1, column=1, sticky="w", padx=10)

            self.cuadroTextoPwd=ttk.Entry(frame, textvariable=self.miPwd).grid(row=2, column=2, padx=5, pady=5)
            self.contraseñaLabel=ttk.Label(frame, text="Contraseña: ").grid(row=2, column=1, sticky="w", padx=10)

            self.cuadroTextoTUser=ttk.Entry(frame, textvariable=self.miTUser).grid(row=3, column=2, padx=5, pady=5)
            self.tipoUserLabel=ttk.Label(frame, text="Tipo usuario: ").grid(row=3, column=1, sticky="w", padx=10)

            s = ttk.Style()
            s.configure("my.TButton", font=("Calibri", 14, "bold"))
            self.btnGuardar=ttk.Button(frame, text="Crear usuario", style="my.TButton", command=self.add_usuario)
            self.btnGuardar.grid(row=4, column=1, columnspan=2, sticky=W+E)

        if opcion==2:
            self.etiqueta_nick_anituguo = ttk.Label(frame, text = "Nick antiguo: ", font=('Calibri', 13)).grid(row=2, column=0)
            self.input_nick_antiguo = ttk.Entry(frame, textvariable=StringVar(self.ventana_editar, value=old_nick), state='readonly', font=('Calibri', 13)).grid(row=2, column=1)
            
            self.etiqueta_nick_nuevo = ttk.Label(frame, text="Nombre nuevo: ", font=('Calibri', 13)).grid(row=3, column=0)
            # Entry Nombre nuevo (texto que si se podra modificar)
            self.input_nick_nuevo = ttk.Entry(frame, font=('Calibri', 13)).grid(row=3, column=1)
            # Label Precio antiguo
            self.etiqueta_precio_anituguo = Label(frame, text="Precio antiguo: ", font=('Calibri', 13))
            self.etiqueta_precio_anituguo.grid(row=4, column=0)
            self.input_precio_antiguo = Entry(frame, textvariable=StringVar(self.ventana_editar, value=old_pwd), state='readonly', font=('Calibri', 13)).grid(row=4, column=1)
            # Label Precio nuevo
            self.etiqueta_precio_nuevo = ttk.Label(frame, text="Precio nuevo: ", font=('Calibri', 13)).grid(row=5, column=0)
            self.input_precio_nuevo = ttk.Entry(frame, font=('Calibri', 13)).grid(row=5, column=1)
            
            # Boton Actualizar Producto
            s = ttk.Style()
            s.configure("my.TButton", font=("Calibri", 14, "bold"))
            self.boton_actualizar = ttk.Button(frame, text="Actualizar", style="my.TButton", command=lambda: self.actualizar_usuario(self.input_nick_nuevo.get(), self.input_nick_antiguo.get(), self.input_precio_nuevo.get(), self.input_precio_antiguo.get())).grid(row=6, columnspan=2, sticky=W + E)

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
        self.miId.set("")
        self.miNick.set("")
        self.miPwd.set("")
        self.miTUser.set("")

    def add_usuario(self):
        conexion=conectarBBDD("localhost","app-vontade","root","")
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO USERS_APLICACION VALUES (NULL,'"+self.miNick.get()+"','"+self.miPwd.get()+"','"+self.miTUser.get()+"')")
        conexion.commit()
        messagebox.showinfo("Nuevo usuario", "Has introducido un usuario")
        cursor.close()
        conexion.close()
        self.limpiarCampos()
        self.actualizarTabla()

    def eliminar_usuario(self):
        self.mensaje["text"]=""
        #Comprobación de que se seleccione un producto para eliminarlo
        try:
            self.tabla.item(self.tabla.selection())["text"][0]
        except IndexError as e:
            self.mensaje["text"]= "Por favor, seleccio ne un producto"
            return

        self.mensaje["text"] = ""
        nombre=self.tabla.item(self.tabla.selection())["text"]
        query="DELETE FROM producto WHERE nombre=?"
        self.db_consulta(query,(nombre, ))
        self.mensaje["text"] = "Producto {} eliminado con éxito.".format(nombre)
        self.get_productos()

    def editar_usuario(self):
        #Comprobación de que se seleccione un producto para editarlo
        try:
            self.tabla.item(self.tabla.selection())["text"]
        except IndexError as e:
            messagebox.showerror("Sin datos", "Por favor, seleccione un usuario")
            return
        
        old_id = self.tabla.item(self.tabla.selection())['text']
        old_nick = self.tabla.item(self.tabla.selection())['values'][0]
        old_pwd = self.tabla.item(self.tabla.selection())['values'][1]
        old_tuser = self.tabla.item(self.tabla.selection())['values'][2]
      
        #Ventana nueva (editar usuario
        self.ventana_editar = Toplevel()  # Crear una ventana por delante de la principal
        self.ventana_editar.title = "Editar Usuario"  # Titulo de la ventana
        self.ventana_editar.resizable(1, 1)
        titulo = Label(self.ventana_editar, text='Edición de Usuario', font=('Calibri', 50, 'bold'))
        titulo.grid(column=0, row=0)
        
        # Creacon del contenedor Frame de la ventana de Editar
        self.frame_editar = LabelFrame(self.ventana_editar, text="Editar el siguiente Producto", font=('Calibri', 16, 'bold')).grid(row=1, column=0, columnspan=20, pady=20)
        
        self.crear_widgets(self.frame_editar, 2)

    def actualizar_usuario(self, nuevo_nombre, antiguo_nombre, nuevo_precio, antiguo_precio):
        conexion=conectarBBDD("localhost","app-vontade","root","")
        cursor=conexion.cursor()
        cursor.execute("INSERT INTO USERS_APLICACION VALUES (NULL,'"+self.miNick.get()+"','"+self.miPwd.get()+"','"+self.miTUser.get()+"')")
        conexion.commit()
        messagebox.showinfo("Nuevo usuario", "Has introducido un usuario")
        cursor.close()
        conexion.close()
        self.limpiarCampos()
        self.actualizarTabla()
        producto_modificado = False
        query = 'UPDATE producto SET nombre = ?, precio = ? WHERE nombre = ? AND precio = ?'
        if nuevo_nombre != '' and nuevo_precio != '':
            # Si el usuario escribe nuevo nombre y nuevo precio, se cambian ambos
            parametros = (nuevo_nombre, nuevo_precio, antiguo_nombre, antiguo_precio)
            producto_modificado = True
        elif nuevo_nombre != '' and nuevo_precio == '':
            # Si el usuario deja vacio el nuevo precio, se mantiene el pecio anterior p
            parametros = (nuevo_nombre, antiguo_precio, antiguo_nombre, antiguo_precio)
            producto_modificado = True
        elif nuevo_nombre == '' and nuevo_precio != '':
            # Si el usuario deja vacio el nuevo nombre, se mantiene el nombre anterior
            parametros = (antiguo_nombre, nuevo_precio, antiguo_nombre, antiguo_precio)
            producto_modificado = True

        if(producto_modificado):
            self.db_consulta(query, parametros)
            self.ventana_editar.destroy() # Cerrar la ventana de edicion de productos
            self.mensaje['text'] = 'El producto {} ha sido actualizado con éxito'.format(antiguo_nombre) # Mostrar mensaje para el usuario
            self.get_productos() # Actualizar la tabla de productos
        else:
            self.ventana_editar.destroy() # Cerrar la ventana de edicion de productos
            self.mensaje['text'] = 'El producto {} NO ha sido actualizado'.format(antiguo_nombre) # Mostrar mensaje para el usuario


root=Tk()
app=CrudPOO(root)
app.mainloop()