nombre = "Alex Alonso"

contador=0

for i in nombre:
    if i == " ":
        continue
    contador+=1

print(nombre+" tiene "+str(contador)+" letras.")

for i in nombre:
    pass

print("Pass no hace nada.")

email="info@alex"

for i in email:
    if i =="@":
        arroba=True
        break
else:
    arroba=False

print(arroba)