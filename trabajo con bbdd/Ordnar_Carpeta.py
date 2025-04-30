import os
import shutil

#ruta carpeta
ruta="C:/Users/Usuario/Desktop/carpeta"

#crear carpetas si no existen
#tipos=["IMG","PDFs", "doc_texto"]
extensiones={
    ".jpg":"IMG",
    ".png":"IMG",
    ".pdf":"PDFs",
    ".txt":"doc_texto",
    ".odt":"doc_texto",
}
for carpeta in set(extensiones.values()):
    nuevaCarpeta=os.path.join(ruta,carpeta)
    if not os.path.exists(nuevaCarpeta):
        os.mkdir(nuevaCarpeta)

for archivo in os.listdir(ruta):
    nuevoArchivo=os.path.join(ruta,archivo)
    if os.path.isfile(nuevoArchivo):
        nane,ext=os.path.splitext(archivo)
        if ext in extensiones:
            destino=os.path.join(ruta,extensiones[ext],archivo)
            shutil.move(nuevoArchivo,destino)