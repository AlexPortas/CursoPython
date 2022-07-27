from tkinter import *

raiz=Tk()

frame=Frame(raiz)

frame.pack()

operacion=""

resultado=0

digitoDisplay=StringVar()

cuadroTextoResultado=Entry(frame, textvariable=digitoDisplay, font=('Arial 22'))

cuadroTextoResultado.grid(row=0, column=0, columnspan=4, pady=5)

cuadroTextoResultado.config(background="black", fg="#00db00", justify="right")

digitoDisplay.set('0')

#-------------------- Funciones
puntoIncluido=False

def clicarTeclas(n):
    global puntoIncluido, operacion
    if digitoDisplay.get()=="" and n=='0':
        return
    if puntoIncluido and n=='.':
        return
    if operacion!='':
        digitoDisplay.set(n)
        operacion=''
    else:
        if digitoDisplay.get()!='0' or n=='.':
            digitoDisplay.set(digitoDisplay.get() + n)
        else:
            digitoDisplay.set(n)
    if n=='.':
        puntoIncluido=True

def suma(oper):
    global operacion, resultado, puntoIncluido
    operacion=oper
    resultado+=float(digitoDisplay.get())
    if resultado.is_integer():
        digitoDisplay.set(int(resultado))
    else:
        digitoDisplay.set(resultado)
    puntoIncluido=False

def total(oper):
    global resultado, operacion, puntoIncluido
    operacion=oper
    resultado+=float(digitoDisplay.get())
    if resultado.is_integer():
        digitoDisplay.set(int(resultado))
    else:
        digitoDisplay.set(resultado)
    resultado=0
    puntoIncluido=False

#-------------------- Primera fila

btn1=Button(frame, text="1", width=10, command=lambda:clicarTeclas("1"))

btn1.grid(row=1, column=0)

btn2=Button(frame, text="2", width=10, command=lambda:clicarTeclas("2"))

btn2.grid(row=1, column=1)

btn3=Button(frame, text="3", width=10, command=lambda:clicarTeclas("3"))

btn3.grid(row=1, column=2)

btnDividir=Button(frame, text="/", width=10, command=lambda:('/'))

btnDividir.grid(row=1, column=3)

#------------ Segunda fila

btn4=Button(frame, text="4", width=10, command=lambda:clicarTeclas("4"))

btn4.grid(row=2, column=0)

btn5=Button(frame, text="5", width=10, command=lambda:clicarTeclas("5"))

btn5.grid(row=2, column=1)

btn6=Button(frame, text="6", width=10, command=lambda:clicarTeclas("6"))

btn6.grid(row=2, column=2)

btnMultiplicar=Button(frame, text="X", width=10, command=lambda:('*'))

btnMultiplicar.grid(row=2, column=3)

#-------------------- Tercera fila

btn7=Button(frame, text="7", width=10, command=lambda:clicarTeclas("7"))

btn7.grid(row=3, column=0)

btn8=Button(frame, text="8", width=10, command=lambda:clicarTeclas("8"))

btn8.grid(row=3, column=1)

btn9=Button(frame, text="9", width=10, command=lambda:clicarTeclas("9"))

btn9.grid(row=3, column=2)

btnRestar=Button(frame, text="-", width=10, command=lambda:('-'))

btnRestar.grid(row=3, column=3)

#------------ Cuarta fila

btnResultado=Button(frame, text="=", width=10, command=lambda:total('='))

btnResultado.grid(row=4, column=0)

btn0=Button(frame, text="0", width=10, command=lambda:clicarTeclas("0"))

btn0.grid(row=4, column=1)

btnPunto=Button(frame, text=".", width=10, command=lambda:clicarTeclas("."))

btnPunto.grid(row=4, column=2)

btnSumar=Button(frame, text="+", width=10, command=lambda:suma('+'))

btnSumar.grid(row=4, column=3)

#------------ Final

raiz.mainloop()