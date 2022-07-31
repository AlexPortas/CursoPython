from tkinter import *

from moduloCalculadoras.operacionesCalc import *  

def construirBotones(self, botones, filas, columnas):
    contador=0
    for fila in range(1,filas+1):
        for columna in range(columnas):
            botones[contador].grid(row=fila, column=columna)
            contador+=1 


def colocarBtn(self, valor, mostrar=True):
    return Button(self.ventana, text=valor, width=10, font=('Courier', 9), command=lambda:pulsacionesTeclas(self, valor, mostrar))
