import PyPDF2

# abrir pdf

with open("C:/Users/Usuario/Desktop/carpeta/Apuntes.pdf", "rb") as archivo:
    lector=PyPDF2.PdfReader(archivo)

    print(f"El pdf tiene {len(lector.pages)} páginas")

    for i,p in enumerate(lector.pages):
        print("Página {}: {}".format(i,p.extract_text()))