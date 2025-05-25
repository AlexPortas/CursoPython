import os

ruta="C:/Users/Usuario/Desktop/carpeta/IMG"
prefijo="imagen_"
extension=(".png",".jpg")

archivos=[]
for f in os.listdir(ruta):
    if f.endswith(extension):
        archivos.append(f)

for i, archivo in enumerate(archivos, start=1):
    ext_actual=os.path.splitext(archivo)[1]
    nombre=f"{prefijo}{i:03}{ext_actual}"
    ruta_actual=os.path.join(ruta,archivo)
    ruta_nueva  =os.path.join(ruta,nombre)
    os.rename(ruta_actual,ruta_nueva)
