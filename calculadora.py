from tkinter import *
from tkinter import messagebox

raiz=Tk()

frame=Frame(raiz)

frame.pack()


cuadroTextoResultado=Entry(frame)

cuadroTextoResultado.grid(row=0, column=0, columnspan=4, pady=5)

cuadroTextoResultado.config(background="black", fg="green", justify="right", width=50)

#-------------------- Primera fila

btn1=Button(frame, text="1", width=10)

btn1.grid(row=1, column=0)

btn2=Button(frame, text="2", width=10)

btn2.grid(row=1, column=1)

btn3=Button(frame, text="3", width=10)

btn3.grid(row=1, column=2)

btnDividir=Button(frame, text="/", width=10)

btnDividir.grid(row=1, column=3)

#------------ Segunda fila

btn4=Button(frame, text="4", width=10)

btn4.grid(row=2, column=0)

btn5=Button(frame, text="5", width=10)

btn5.grid(row=2, column=1)

btn6=Button(frame, text="6", width=10)

btn6.grid(row=2, column=2)

btnMultiplicar=Button(frame, text="X", width=10)

btnMultiplicar.grid(row=2, column=3)

#-------------------- Tercera fila

btn7=Button(frame, text="7", width=10)

btn7.grid(row=3, column=0)

btn8=Button(frame, text="8", width=10)

btn8.grid(row=3, column=1)

btn9=Button(frame, text="9", width=10)

btn9.grid(row=3, column=2)

btnRestar=Button(frame, text="-", width=10)

btnRestar.grid(row=3, column=3)

#------------ Cuarta fila

btnResultado=Button(frame, text="=", width=10)

btnResultado.grid(row=4, column=0)

btn0=Button(frame, text="0", width=10)

btn0.grid(row=4, column=1)

btnPunto=Button(frame, text=".", width=10)

btnPunto.grid(row=4, column=2)

btnSumar=Button(frame, text="+", width=10)

btnSumar.grid(row=4, column=3)

#------------ Final

raiz.mainloop()