class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
            
    def hablar(self):
        return self.nombre + " está hablando"

    def pensar(self):
        return self.nombre + " está pensando"
    
    def caminar(self):
        return self.nombre + " está caminando"

    def comer(self):
        return self.nombre + " está comiendo" 
        
    def getDatos(self):
        return "Nombre: " + self.nombre + ", apellido: " + self.apellido +", edad: " + str(self.edad)
    
class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad, empresa):
        Persona.__init__(self, nombre, apellido, edad)
        self.empresa = empresa
        
    def getDatos(self):
        return super().getDatos() + ", empresa: " + self.empresa

    def trabajar(self):
        return self.nombre + " está trabajando"
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, escuela):
        Persona.__init__(self, nombre, apellido, edad)
        self.escuela = escuela
        
    def getDatos(self):
        return super().getDatos() + ", escuela: " + self.escuela

    def estudiar(self):
        return self.nombre + " está estudiando"

class Director(Trabajador, Estudiante):
    def __init__(self, nombre, apellido, edad, empresa, escuela, sueldo):
        Trabajador.__init__(self, nombre, apellido, edad, empresa)
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.sueldo = sueldo
        
    def getDatos(self):
        return super().getDatos() + ", salario: " + str(self.sueldo)

    def dirigir(self):
        return self.nombre + " está dirigiendo"

p1 = Persona("Alex", "alonso", 27)

e1 = Estudiante("Juan", "Diaz", 17, "IES Teis")

t1 = Trabajador("Samu", "Diaz", 37, "Cope")

d1 = Director("Carlos", "Sanchez", 55, "AIG", "IES Tomiño", 3500)

print(p1.getDatos())

print(e1.getDatos())

print(t1.getDatos())

print(d1.getDatos())