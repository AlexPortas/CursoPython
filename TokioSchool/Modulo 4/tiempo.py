from datetime import datetime, date, time, timedelta

# El objeto datetime

dt = datetime.now() # Ahora

print(dt)
print(dt.year) # año
print(dt.month) # mes
print(dt.day) # día
print(dt.hour) # hora
print(dt.minute) # minutos
print(dt.second) # segundos
print(dt.microsecond) # microsegundos
print(dt.tzinfo) # zona horaria, nula por defecto

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))

# Crear un datetime manualmente (year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

dt = datetime(2019, 2, 28, 10, 15, 00, 00000)
print(dt)

dt = dt.replace(year=3000) # Asignación correcta con .replace()
print(dt)

# Comparando fechas y horas: datetime.time() y date.today()

print("Horas:")
hora1 = time(10, 5, 0)  # Asigna 10h 5m 0s
print("\tHora1:", hora1)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\tHora2:", hora2)

# Compara horas
print("\tHora1 < Hora2:", hora1 < hora2)  # True

print("Fechas:")
fecha1 = date.today()  # Asigna fecha actual
print("\tFecha1:", fecha1)

# Suma a la fecha actual 2 días
fecha2 = date.today() + timedelta(days=2)
print("\tFecha2:", fecha2)

# Compara fechas
print("\tFecha1 > Fecha2:", fecha1 > fecha2)  # False

# Formato automático ISO (Organización Internacional de Normalización) 

dt = datetime.now()
print(dt)

print(dt.isoformat())

### Formateo munual (inglés por defecto)

print(dt.strftime("%A %d %B %Y %I:%M"))

# Sumando y restando tiempo con timedelta

dt = datetime.now()
print(dt)

t = timedelta(days=14, hours=4, seconds=1000)
print(t)

dentro_de_dos_semanas = dt + t
print(dentro_de_dos_semanas)
print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))

hace_dos_semanas = dt - t
print(hace_dos_semanas)
print(hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))