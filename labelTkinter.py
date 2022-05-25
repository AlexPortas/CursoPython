import tkinter

raiz = tkinter.Tk()

frame = tkinter.Frame(raiz, width=500, height=400)

frame.pack()

#info = tkinter.Label(frame, text="esto es una prueba")

#info.place(x=120, y=200)

tkinter.Label(frame, text="esto es una prueba").place(x=120, y=200)

raiz.mainloop()