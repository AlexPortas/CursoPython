datos = ("Alex", 24, 2, 1993)

print(datos)

datosLista = list(datos)

print(datosLista)

datosTupla = tuple(datosLista)

print(datosTupla)

print(24 in datosTupla)

print(datosTupla.count("Alex"))

print(len(datosTupla))

nombre, diaMac, mesNac, anhoNac = datosTupla

print(nombre+" "+str(diaMac)+" "+str(mesNac))