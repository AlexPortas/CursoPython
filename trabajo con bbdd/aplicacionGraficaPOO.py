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
        

        #botones eliminar y editar
        s=ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))

        self.btnEliminar=ttk.Button(text="ELIMINAR", style="my.TButton")#, command=self.eliminar_usuario)
        self.btnEliminar.grid(row=5, column=0, sticky=W+E)
        self.btnEditar=ttk.Button(text="EDITAR", style="my.TButton")#, command=self.editar_usuario)
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

    def crear_widgets(self, frame):
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
        self.mensaje["text"]=""
        #Comprobación de que se seleccione un producto para editarlo
        try:
            self.tabla.item(self.tabla.selection())["text"][0]
        except IndexError as e:
            self.mensaje["text"]= "Por favor, seleccione un producto"
            return
        
        old_nombre = self.tabla.item(self.tabla.selection())['text']
        old_precio = self.tabla.item(self.tabla.selection())['values'][0]
        print("old_nombre", self.tabla.item(self.tabla.selection())['text'],"old_precio" ,self.tabla.item(self.tabla.selection())['values'][0])
        #Ventana nueva (editar producto
        self.ventana_editar = Toplevel()  # Crear una ventana por delante de la principal
        self.ventana_editar.title = "Editar Producto"  # Titulo de la ventana
        self.ventana_editar.resizable(1, 1)
        self.ventana_editar.wm_iconbitmap('recursos/logo.ico')
        titulo = Label(self.ventana_editar, text='Edición de Productos', font=('Calibri', 50, 'bold'))
        titulo.grid(column=0, row=0)
        
        # Creacion del contenedor Frame de la ventana de Editar Producto
        frame_ep = LabelFrame(self.ventana_editar, text="Editar el siguiente Producto", font=('Calibri', 16, 'bold'))
        frame_ep.grid(row=1, column=0, columnspan=20, pady=20)
        
        # Label Nombre antiguo
        self.etiqueta_nombre_anituguo = Label(frame_ep, text = "Nombre antiguo: ", font=('Calibri', 13))
        self.etiqueta_nombre_anituguo.grid(row=2, column=0)
        # Entry Nombre antiguo (texto que no se podra modificar)
        self.input_nombre_antiguo = Entry(frame_ep, textvariable=StringVar(self.ventana_editar, value=old_nombre), state='readonly', font=('Calibri', 13))
        self.input_nombre_antiguo.grid(row=2, column=1)
        # Label Nombre nuevo
        self.etiqueta_nombre_nuevo = Label(frame_ep, text="Nombre nuevo: ", font=('Calibri', 13))
        self.etiqueta_nombre_nuevo.grid(row=3, column=0)
        # Entry Nombre nuevo (texto que si se podra modificar)
        self.input_nombre_nuevo = ttk.Entry(frame_ep, font=('Calibri', 13))
        self.input_nombre_nuevo.grid(row=3, column=1)
        self.input_nombre_nuevo.focus() # Para que el foco del raton vaya a este Entry al inicio
        # Label Precio antiguo
        self.etiqueta_precio_anituguo = Label(frame_ep, text="Precio antiguo: ", font=('Calibri', 13))
        self.etiqueta_precio_anituguo.grid(row=4, column=0)
        # Entry Precio antiguo (texto que no se podra modificar)
        self.input_precio_antiguo = Entry(frame_ep, textvariable=StringVar(self.ventana_editar, value=old_precio), state='readonly', font=('Calibri', 13))
        self.input_precio_antiguo.grid(row=4, column=1)
        # Label Precio nuevo
        self.etiqueta_precio_nuevo = Label(frame_ep, text="Precio nuevo: ", font=('Calibri', 13))
        self.etiqueta_precio_nuevo.grid(row=5, column=0)
        # Entry Precio nuevo (texto que si se podra modificar)
        self.input_precio_nuevo = ttk.Entry(frame_ep, font=('Calibri', 13))
        self.input_precio_nuevo.grid(row=5, column=1)
        
        # Boton Actualizar Producto
        s = ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))
        self.boton_actualizar = ttk.Button(frame_ep, text="Actualizar Producto", style="my.TButton", command=lambda: self.actualizar_productos(self.input_nombre_nuevo.get(), self.input_nombre_antiguo.get(), self.input_precio_nuevo.get(), self.input_precio_antiguo.get()))
        self.boton_actualizar.grid(row=6, columnspan=2, sticky=W + E)

    def actualizar_usuario(self, nuevo_nombre, antiguo_nombre, nuevo_precio, antiguo_precio):
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