capitales = {"España":"Madrid","Francia":"Paris","Italia":"Roma", "China":"Pekin", "Japon":"Tokio"}

for clave in capitales:
    print(clave+" -> "+capitales[clave])

print(capitales.items())

for clave, valor in capitales.items():
    print(clave+" -> "+valor)