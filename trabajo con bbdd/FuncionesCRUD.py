from tkinter import Button, Entry, Frame, Label, Menu, StringVar, Tk, Toplevel, simpledialog, messagebox
from ConexionesBBDD import *
from aplicacionGraficaPOO import *

def add_usuario(variables):
    conexion=conectarBBDD("localhost","app-vontade","root","")
    #cursor.execute("INSERT INTO USERS_APLICACION VALUES (NULL,'"+self.miNick.get()+"','"+self.miPwd.get()+"','"+self.miTUser.get()+"')")
    datos=variables[:3]
    #cursor.execute("INSERT INTO USERS_APLICACION VALUES (NULL,?,?,?)", datos)
    db_consulta(conexion,"INSERT INTO USERS_APLICACION (nick, pwd, tipo) VALUES (?, ?, ?)", (datos))
    messagebox.showinfo("Nuevo usuario", "Has introducido un usuario")
    conexion.close()
    limpiarCampos()
    actualizarTabla()

def eliminar_usuario(self):
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
    cursor.execute("UPDATE USERS_APLICACION SET nick=?, pwd=?, tipo=? WHERE ID=?", (nick, pwd, tuser, id))
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