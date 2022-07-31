from tkinter import *

def mostrarDisplay(self, valor):
    self.display.insert(END, valor)

def borrarDisplay(self):
    self.display.delete(0, END)