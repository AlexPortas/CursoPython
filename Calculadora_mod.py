from tkinter import *

from moduloCalculadoras.botoneraCalc import *  

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
        btn1=colocarBtn(self, 1)
        btn2=colocarBtn(self, 2)
        btn3=colocarBtn(self, 3)
        btnDiv=colocarBtn(self, '/')

        btn4=colocarBtn(self, 4)
        btn5=colocarBtn(self, 5)
        btn6=colocarBtn(self, 6)
        btnMult=colocarBtn(self, u"\u00d7")

        btn7=colocarBtn(self, 7)
        btn8=colocarBtn(self, 8)
        btn9=colocarBtn(self, 9)
        btnRest=colocarBtn(self, '-')

        btnResul=colocarBtn(self, '=', mostrar=False)
        btn0=colocarBtn(self, 0)
        btnComa=colocarBtn(self, '.')
        btnSum=colocarBtn(self, '+')

        botones=[btn1, btn2, btn3, btnDiv, btn4, btn5, btn6, btnMult, btn7, btn8, btn9, btnRest, btnResul, btn0, btnComa, btnSum]
        
        construirBotones(self, botones, 4, 4) 

        mostrarDisplay(self, '0')

calcu = Calculadora(raiz)

raiz.mainloop()