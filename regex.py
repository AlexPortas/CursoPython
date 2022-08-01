import re 

cadena="Estoy trabajando en Python en domingo y semana santa. Python es bastante sencillo"
busqueda="Python"

if re.search(busqueda, cadena) is not None:
    print("Se encontro ", busqueda)
else:
    print("No se encontro ", busqueda)

texto=re.search(busqueda, cadena)

print(texto.start())
print(texto.end())
print(texto.span())


print(len(re.findall(busqueda,cadena)))

nombres=["Alaba", "Valverde", "Kroos", "Vinicius", "alaba"]

for n in nombres:
    if re.findall("^V", n):
        print(n)

for n in nombres:
    if re.findall("s$", n):
        print(n)

for n in nombres:
    if re.findall("[Aa]laba", n):
        print(n)