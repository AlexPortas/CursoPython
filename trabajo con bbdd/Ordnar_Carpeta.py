import os
import shutil

#ruta carpeta
ruta="C:/Users/Usuario/Desktop/carpeta"

#crear carpetas si no existen
tipos=["IMG","PDFs", "doc_texto"]

for carpeta in tipos:
    nuevaCarpeta=os.path.join(ruta,carpeta)
    if not os.path.exists(nuevaCarpeta):
        os.mkdir(nuevaCarpeta)

for archivo in os.listdir(ruta):
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"IMG"))
    if archivo.endswith(".pdf"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"PDFsG"))
    if archivo.endswith(".doc") or archivo.endswith(".odt"):
        shutil.move(os.path.join(ruta,archivo),os.path.join(ruta,"doc_texto"))