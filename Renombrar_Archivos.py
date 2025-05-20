import os

ruta="C:/Users/Usuario/Desktop/carpeta/IMG"
prefijo="imagen_"
extension=".jpg"

archivos=[]
for f in os.listdir(ruta):
    if f.endswith(extension):
        archivos.append(f)