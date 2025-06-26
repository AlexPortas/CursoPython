import os
# from docx2pdf import convert
import subprocess
from tkinter import Tk, filedialog

root=Tk()
root.withdraw()

carpeta_entrada=filedialog.askdirectory(title="Selecione una carpeta")
salida=os.path.join(carpeta_entrada,"pdf")

os.makedirs(salida,exist_ok=True)

for archivo in os.listdir(carpeta_entrada):
    # if archivo.endswith(".docx"):
    #     ruta_docx=os.path.join(carpeta_entrada,archivo)
    #     ruta_pdf=os.path.join(carpeta_entrada,archivo.replace(".docx",".pdf"))
    #     convert(ruta_docx,ruta_pdf)
    if archivo.endswith(".odt"):
        ruta_odt=os.path.join(carpeta_entrada,archivo)
        comando = [
             r"C:\Program Files\LibreOffice\program\soffice.exe", "--headless", "--convert-to", "pdf", ruta_odt, "--outdir", salida
        ]
        print(comando, ruta_odt)
        subprocess.run(comando)
        print(f"Convertido: {archivo} → PDF")