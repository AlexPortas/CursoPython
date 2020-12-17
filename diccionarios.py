capitales = {"España":"Madrid","Francia":"Paris","Italia":"Roma"}

print(capitales)

capitales["Portugal"]="Lisboa"

print(capitales)

del capitales["Francia"]

print(capitales)

claves=["Reino Unido", "Alemania"]

capitales[claves[0]]="Londres"

capitales[claves[1]]="Berlin"

print(capitales)

print(capitales.keys())

print(capitales.values())

print(len(capitales))