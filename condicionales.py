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