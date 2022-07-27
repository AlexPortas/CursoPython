from tkinter import *

raiz=Tk()

class Calculadora:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title('Calculadora')

        #agregar display
        self.display=Entry(ventana, font=('Arial 22'))

        #ubicar y formatear display
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        self.display.config(background="black", fg="#00db00", justify="right")

        #creacion botones
        btn1=self.colocarBtn(1)
        btn2=self.colocarBtn(2)
        btn3=self.colocarBtn(3)
        btnDiv=self.colocarBtn('/', mostrar=False)

        btn4=self.colocarBtn(4)
        btn5=self.colocarBtn(5)
        btn6=self.colocarBtn(6)
        btnMult=self.colocarBtn('*', mostrar=False)

        btn7=self.colocarBtn(7)
        btn8=self.colocarBtn(8)
        btn9=self.colocarBtn(9)
        btnRest=self.colocarBtn('-', mostrar=False)

        btnResul=self.colocarBtn('=', mostrar=False)
        btn0=self.colocarBtn(0)
        btnComa=self.colocarBtn('.')
        btnSum=self.colocarBtn('+', mostrar=False)

        botones=[btn1, btn2, btn3, btnDiv, btn4, btn5, btn6, btnMult, btn7, btn8, btn9, btnRest, btnResul, btn0, btnComa, btnSum]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador+=1 

    def colocarBtn(self, valor, mostrar=True):
        return Button(self.ventana, text=valor, width=10, font=('Courier', 9))

calcu= Calculadora(raiz)

raiz.mainloop()