import os
import tkinter as tk
from tkinter import filedialog, messagebox


def selecionar_carpeta():
    ruta=filedialog.askdirectory()
    entrada_carpeta.insert(0,ruta)

def renombrar_archivos():
    ruta=entrada_carpeta.get()
    prefijo=entrada_prefijo.get()
    extension=tuple(entrada_extensiones.get().split(","))

    archivos=[]
    for f in os.listdir(ruta):
        if f.endswith(extension):
            archivos.append(f)

    # creación del archivo .bat
    ruta_deshacer=os.path.join(ruta,"deshacer.bat")
    
    with open(ruta_deshacer, "w", encoding="utf-8") as deshacer:
        for i, archivo in enumerate(archivos, start=1):
            ext_actual=os.path.splitext(archivo)[1]
            nombre=f"{prefijo}{i:03}{ext_actual}"
            ruta_actual=os.path.join(ruta,archivo)
            ruta_nueva=os.path.join(ruta,nombre)
            os.rename(ruta_actual,ruta_nueva)
            deshacer.write(f'rename "{nombre}" "{archivo}"\n')
        deshacer.write(f"del \"%~f0\"\n")
    
    messagebox.showinfo("Éxito", f"Renombrado completo")

# interfaz grafica

ventana = tk.Tk()
ventana.title("Renombrar archivos")
ventana.geometry("400x250")
ventana.resizable(False, False)

tk.Label(ventana,text="Ruta carpeta: ").pack(pady=5)
frame_carpeta = tk.Frame(ventana)
frame_carpeta.pack()
entrada_carpeta=tk.Entry(frame_carpeta, width=40)
entrada_carpeta.pack(side=tk.LEFT,padx=5)
tk.Button(frame_carpeta, text="Examinar", command=selecionar_carpeta).pack(side=tk.LEFT)

tk.Label(ventana,text="Prefijo dos archivos: ").pack(pady=5)
entrada_prefijo=tk.Entry(ventana, width=30)
entrada_prefijo.insert(0, "Imagen_")
entrada_prefijo.pack()

tk.Label(ventana,text="Extensiones (separadas por ,): ").pack(pady=5)
entrada_extensiones=tk.Entry(ventana, width=30)
entrada_extensiones.insert(0, ".jpg,.png")
entrada_extensiones.pack()


tk.Button(ventana, text="Renombrar", command=renombrar_archivos, bg="#04ba04", fg="white", padx=10).pack(pady=15)

ventana.mainloop()