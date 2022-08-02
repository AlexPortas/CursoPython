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

nombres=["Alaba", "Valverde", "Kroos", "Vinicius", "alaba", "Bale"]

for n in nombres:
    if re.findall("^V", n):
        print(n)

for n in nombres:
    if re.findall("s$", n):
        print(n)

for n in nombres:
    if re.findall("[Aa]laba", n):
        print(n)
    
for n in nombres:
    if re.findall("[p-z]", n):
        print(n)

for n in nombres:
    if re.findall("^[A-F]", n):
        print(n)

terminos=["Ma1", "Vi1", "Bi1", "Vi2", "Ma2", "Ba1", "Ma.3", "Ma4", "Viall"]

for n in terminos:
    if re.findall("Ma[^1-3]", n):
        print(n)

for n in terminos:
    if re.findall("Ma[1-3]", n):
        print(n)

for n in terminos:
    if re.findall("Vi[1-3a-z]", n):
        print(n)

n1="jara López"
n2="Juan Diaz"
n3="Alex Alonso"

if re.match("juan", n2, re.IGNORECASE):
    print("Lo encontre")
else:
    print("No lo encontre")
    
if re.search("l[oó]pez", n1, re.IGNORECASE):
    print("Lo encontre")
else:
    print("No lo encontre")