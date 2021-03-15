import datetime

hoy = datetime.date.today()

print(str(hoy))
print(repr(hoy))

class Agenda():
    def __init__(self):
        self.agenda = {}
    
    def agregar(self, n, t):
        self.agenda[n] = t
        
    def borrar(self, n):
        del(self.agenda[n])

    def __str__(self):
        return str(self.agenda)

    def __len__(self):
        return len(self.agenda)

a = Agenda()
a.agregar("Alex",32)
a.agregar("Juan","npi")
a.agregar("maria",12)
a.agregar("martin",1)
print(a)
print(len(a))
a.borrar("martin")
print(a)
print(len(a))

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Datos persona \nNombre: " + str(self.nombre) + "\nEdad: " +str(self.edad)

p1 = Persona("Alex", 28)

print(p1)