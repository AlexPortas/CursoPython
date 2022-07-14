from tkinter import *
from tkinter import messagebox

raiz=Tk()

frame=Frame(raiz, width=1000, height=700)

frame.pack()


cuadroTextoResultado=Entry(frame)

cuadroTextoResultado.grid(row=0, column=1, padx=15, pady=15)

cuadroTextoResultado.config(background="black", fg="green", justify="right")

#-------------------- Primera fila
def funcionClick():
    messagebox.showinfo("Saludo", "Hola " + cuadroTextoResultado.get())

btn1=Button(raiz, text="1", width=10, wicommand=funcionClick)

btn1.grid(row=1, column=0)

btn2=Button(raiz, text="2", width=10, command=funcionClick)

btn2.grid(row=1, column=1)

btn3=Button(raiz, text="3", width=10, command=funcionClick)

btn3.grid(row=1, column=2)

btnDividir=Button(raiz, text="/", width=10, command=funcionClick)

btnDividir.grid(row=1, column=3)

#------------ Segunda fila

btn4=Button(raiz, text="4", width=10, command=funcionClick)

btn4.grid(row=2, column=0)

raiz.mainloop()