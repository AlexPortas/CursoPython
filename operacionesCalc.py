from tkinter import *
import re

from operacionesDisplayCalc import *  

def pulsacionesTeclas(self, valor, mostrar):
    if self.operacion=='' and valor==0:
        return
    if self.operacion=='' and valor!=0:
        borrarDisplay(self)    
    if self.puntoIncluido and valor=='.':
        return
    if mostrar:
        if self.resultado and str(valor).isdigit():
            borrarDisplay(self)
            self.operacion=str(valor)
            mostrarDisplay(self, valor)
        else:
            self.operacion+=str(valor)
            mostrarDisplay(self, valor)
        self.resultado=False
    else:
        self.operacion=re.sub(u"\u00d7", "*", self.operacion)
        borrarDisplay(self)
        mostrarDisplay(self, str(eval(self.operacion)))
        self.puntoIncluido=False
        self.resultado=True
        self.operacion=str(eval(self.operacion))
    if valor=='.':
        self.puntoIncluido=True     