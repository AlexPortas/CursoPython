from tkinter import *
import mysql.connector

class CrudPOO(Frame):
    def __init__(self, raiz):
        # ----- Variables de control
        self.miId=StringVar()
        self.miNick=StringVar()
        self.miPwd=StringVar()
        self.miTUser=StringVar()
        self.miNombre=StringVar()
        self.miCorreo=StringVar()

        super().__init__(raiz)
        self.master=raiz
        self.pack()

        self.crear_widgets()

    def crear_widgets(self):
        self.cuadroTextoId=Entry(self, textvariable=self.miId).grid(row=0, column=1, padx=5, pady=5)
        self.idLabel=Label(self, text="Id: ").grid(row=0, column=0, sticky="w", padx=10)

        self.cuadroTextoNick=Entry(self, textvariable=self.miNick).grid(row=1, column=1, padx=5, pady=5)
        self.nickLabel=Label(self, text="Nick: ").grid(row=1, column=0, sticky="w", padx=10)

        self.cuadroTextoPwd=Entry(self, textvariable=self.miPwd).grid(row=2, column=1, padx=5, pady=5)
        self.contraseñaLabel=Label(self, text="Contraseña: ").grid(row=2, column=0, sticky="w", padx=10)

        self.cuadroTextoTUser=Entry(self, textvariable=self.miTUser).grid(row=3, column=1, padx=5, pady=5)
        self.tipoUserLabel=Label(self, text="Tipo usuario: ").grid(row=3, column=0, sticky="w", padx=10)

        self.cuadroTextoNombre=Entry(self, textvariable=self.miNombre).grid(row=4, column=1, padx=5, pady=5)
        self.nombreLabel=Label(self, text="Nombre: ").grid(row=4, column=0, sticky="w", padx=10)

        self.cuadroTextoCorreo=Entry(self, textvariable=self.miCorreo).grid(row=5, column=1, padx=5, pady=5)
        self.correoLabel=Label(self, text="Dirección electronica: ").grid(row=5, column=0, sticky="w", padx=10)


root=Tk()
app=CrudPOO(root)
app.mainloop()