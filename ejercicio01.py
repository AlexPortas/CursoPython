tipoRenta = int(input("Introduce cuanto ganas al año: "))

if tipoRenta > 70000:
    porcentaje = "45%"
elif 35000 < tipoRenta < 70000:
    porcentaje = "35%"
elif 18000 < tipoRenta < 35000:
    porcentaje = "21%"
elif 12000 < tipoRenta < 18000:
    porcentaje = "15%"
elif tipoRenta < 12000:
    porcentaje = "7%"

print("A la renta " + str(tipoRenta) + " le corresponde " + porcentaje + " del tipo impositivo.")