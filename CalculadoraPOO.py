from tkinter import *
import re

raiz=Tk()

class Calculadora:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title('Calculadora')
        self.operacion = ""
        self.puntoIncluido = False
        self.resultado = False

        #agregar display
        self.display=Entry(ventana, font=('Arial 22'))

        #ubicar y formatear display
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        self.display.config(background="black", fg="#00db00", justify="right")

        #creacion botones
        btn1=self.colocarBtn(1)
        btn2=self.colocarBtn(2)
        btn3=self.colocarBtn(3)
        btnDiv=self.colocarBtn('/')

        btn4=self.colocarBtn(4)
        btn5=self.colocarBtn(5)
        btn6=self.colocarBtn(6)
        btnMult=self.colocarBtn(u"\u00d7")

        btn7=self.colocarBtn(7)
        btn8=self.colocarBtn(8)
        btn9=self.colocarBtn(9)
        btnRest=self.colocarBtn('-')

        btnResul=self.colocarBtn('=', mostrar=False)
        btn0=self.colocarBtn(0)
        btnComa=self.colocarBtn('.')
        btnSum=self.colocarBtn('+')

        botones=[btn1, btn2, btn3, btnDiv, btn4, btn5, btn6, btnMult, btn7, btn8, btn9, btnRest, btnResul, btn0, btnComa, btnSum]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1 

        self.mostrarDisplay('0')

    def colocarBtn(self, valor, mostrar=True):
        return Button(self.ventana, text=valor, width=10, font=('Courier', 9), command=lambda:self.pulsacionesTeclas(valor, mostrar))

    def pulsacionesTeclas(self, valor, mostrar):
        if self.operacion=='' and valor==0:
            return
        if self.operacion=='' and valor!=0:
            self.borrarDisplay()
        if self.puntoIncluido and valor=='.':
            return
        if mostrar:
            if self.resultado and str(valor).isdigit():
                self.borrarDisplay()
                self.operacion=str(valor)
                self.mostrarDisplay(valor)
            else:
                self.operacion+=str(valor)
                self.mostrarDisplay(valor)
            self.resultado=False
        else:
            self.operacion=re.sub(u"\u00d7", "*", self.operacion)
            self.borrarDisplay()
            self.mostrarDisplay(str(eval(self.operacion)))
            self.puntoIncluido=False
            self.resultado=True
            self.operacion=str(eval(self.operacion))
        if valor=='.':
            self.puntoIncluido=True               

    def mostrarDisplay(self, valor):
        self.display.insert(END, valor)

    def borrarDisplay(self):
        self.display.delete(0, END)

calcu = Calculadora(raiz)

raiz.mainloop()