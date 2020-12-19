def evaluarAlumno(nota):
    if nota > 10:
        valoracion = "nota incorrecta"
    else:
        if nota == 10:
            valoracion = "matricula"
        elif nota == 9:
            valoracion = "sobresaliente"
        elif nota == 7 or nota == 8:
            valoracion = "notable"
        elif nota == 6:
            valoracion = "bien"
        elif nota == 5:
            valoracion = "aprobado"
        else:
            valoracion = "suspenso"
    return valoracion

notaAlumno = int(input("Introduce la nota: "))

print(evaluarAlumno(notaAlumno))

trabajadores = ["Alex", "Ana", "Dani", "Alba", "Samu"]

if "Pedro" in trabajadores:
    print("Está en la lista")
else:
    print("No está en la lista")
    
lenguajes = "Java, Python, Php"

if "Php" in lenguajes:
    print("Está en el string")
else:
    print("No está en el string")
    
if "SQL" not in lenguajes:
    print("No está en el string")
else:
    print("E3stá en el string")