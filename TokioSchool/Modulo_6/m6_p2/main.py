from tkinter import *
import sqlite3
from tkinter import ttk


class Producto():

    db="database/productos.db"

    def __init__(self, root):
        self.ventana = root
        self.ventana.title("App Gestor de Productos")
        self.ventana.resizable(1,1)
        self.ventana.wm_iconbitmap("recursos/logo.ico")

        #creacion del contenedor frame principal
        frame=LabelFrame(self.ventana, text="Registrar nuevo producto", font=('Calibri', 16, 'bold'))
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        self.etiqueta_nombre=ttk.Label(frame,text="Nombre: ", font=('Calibri', 13))
        self.etiqueta_nombre.grid(row=1, column=0)
        self.nombre=ttk.Entry(frame, font=('Calibri', 13))
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)
        self.etiqueta_precio=ttk.Label(frame,text="Precio: ", font=('Calibri', 13))
        self.etiqueta_precio.grid(row=2, column=0)
        self.precio=ttk.Entry(frame, font=('Calibri', 13))
        self.precio.grid(row=2, column=1)
        s = ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))
        self.btnGuardar=ttk.Button(frame, text="Guardar producto", command=self.add_producto, style="my.TButton")
        self.btnGuardar.grid(row=3, columnspan=2, sticky=W+E)

        self.mensaje=Label(text="", fg="red", font=('Calibri', 13))
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky=W+E)

        # tabla productos

        #estilo personalizado
        style=ttk.Style()
        style.configure("mystyle.Treeview", highlighthickness=0, bg=0, font=("Calibri", 11))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 13, "bold"))
        style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky": "nswe"})])

        self.tabla=ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.tabla.grid(row=4, columnspan=2)
        self.tabla.heading("#0", text="Nombre del producto", anchor=CENTER)
        self.tabla.heading("#1", text="Precio del producto", anchor=CENTER)

        #botones eliminar y editar
        s=ttk.Style()
        s.configure("my.TButton", font=("Calibri", 14, "bold"))

        self.btnEliminar=ttk.Button(text="ELIMINAR", style="my.TButton", command=self.eliminar_producto)
        self.btnEliminar.grid(row=5, column=0, sticky=W+E)
        self.btnEditar=ttk.Button(text="EDITAR", style="my.TButton", command=self.editar_producto)
        self.btnEditar.grid(row=5, column=1, sticky=W+E)

        self.get_productos()

    def db_consulta(self, query, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor=con.cursor()
            resultado=cursor.execute(query, parametros)
            con.commit()
        return resultado

    def get_productos(self):
        registros_tabla=self.tabla.get_children()
        for fila in registros_tabla:
            self.tabla.delete(fila)

        query="SELECT * FROM producto"
        productos=self.db_consulta(query)
        for p in productos:
            print(p)
            self.tabla.insert("", 0, text=p[1], values=p[2])

    def validacion_nombre(self):
        nombre_introducido=self.nombre.get()
           return len(nombre_introducido) != 0

    def validacion_precio(self):
        precio_introducido=self.precio.get()
        return len(precio_introducido) != 0

    def add_producto(self):
        if self.validacion_nombre() and self.validacion_precio():
            query="INSERT INTO producto VALUES (NULL,?,?)"
            parametros=(self.nombre.get(), self.precio.get())
            self.db_consulta(query,parametros)
            self.mensaje["text"]="Producto {} añadido con éxito".format(self.nombre.get())
            self.nombre.delete(0, END)
            self.precio.delete(0, END)
        else:
            self.mensaje["text"]="Datos no introducidos correctamente"

        self.get_productos()

    def eliminar_producto(self):
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

    def editar_producto(self):
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

    def actualizar_productos(self, nuevo_nombre, antiguo_nombre, nuevo_precio, antiguo_precio):
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

if __name__ == '__main__':
    root=Tk()
    app=Producto(root)
    root.mainloop()

