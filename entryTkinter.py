from tkinter import *

raiz=Tk()

frame=Frame(raiz, width=1000, height=700)

frame.pack()

cuadroTextoNombre=Entry(frame)

cuadroTextoNombre.grid(row=0, column=1, padx=15, pady=15)

nombreLabel=Label(frame, text="Nombre: ")

nombreLabel.grid(row=0, column=0, sticky="w")

cuadroTextoApel=Entry(frame)

cuadroTextoApel.grid(row=1, column=1, padx=15, pady=15)

apellidosLabel=Label(frame, text="Apellidos: ")

apellidosLabel.grid(row=1, column=0, sticky="w",padx=15)

cuadroTextoPwd=Entry(frame)

cuadroTextoPwd.grid(row=2, column=1, padx=15, pady=15)

cuadroTextoPwd.config(show="*")

pwdLabel=Label(frame, text="Contraseña: ")

pwdLabel.grid(row=2, column=0, sticky="w",padx=15)

cuadroTextoTel=Entry(frame)

cuadroTextoTel.grid(row=3, column=1, padx=15, pady=15)

telefonoLabel=Label(frame, text="Teléfono: ")

telefonoLabel.grid(row=3, column=0, sticky="w")

cuadroTextoCorreo=Entry(frame)

cuadroTextoCorreo.grid(row=4, column=1, padx=15, pady=15)

correoLabel=Label(frame, text="Durección electronica: ")

correoLabel.grid(row=4, column=0, sticky="w")

cuadroTextoComentario=Text(frame, width=15, height=10)

cuadroTextoComentario.grid(row=5, column=1, padx=15, pady=15)

comentarioLabel=Label(frame, text="Comentario: ")

comentarioLabel.grid(row=5, column=0, sticky="w")

btnEnviar=Button(frame, text="Enviar")

btnEnviar.grid(row=6, column=1)

raiz.mainloop()