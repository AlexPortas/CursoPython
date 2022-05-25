from tkinter import *

raiz=Tk()

raiz.title("Primera ventana tkinter")

raiz.resizable(0,0)

# cambiar imagen!! tiene que ser un .ico!!  raiz.iconbitmap("favicon.ico")

raiz.config(bg="blue")

# crear marco

frame = Frame()

frame.pack()

frame.config(bg="red")

frame.config(width="650", height="400")

raiz.mainloop()