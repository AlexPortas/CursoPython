from tkinter import *
from tkinter import messagebox

raiz=Tk()

frame=Frame(raiz, width=1000, height=700)

frame.pack()


cuadroTextoResultado=Text(frame, width=25, height=10)

cuadroTextoResultado.grid(row=0, column=1, padx=15, pady=15)


def funcionClick():
    messagebox.showinfo("Saludo", "Hola " + cuadroTextoResultado.get())

btn1=Button(raiz, text="1", command=funcionClick)

btn1.grid(row=1, column=0)

btn2=Button(raiz, text="2", command=funcionClick)

btn2.grid(row=1, column=1)

btn3=Button(raiz, text="3", command=funcionClick)

btn3.grid(row=1, column=2)

btn4=Button(raiz, text="4", command=funcionClick)

btn4.grid(row=2, column=0)

raiz.mainloop()