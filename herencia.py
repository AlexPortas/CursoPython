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
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, escuela):
        super().__init__(nombre,apellido, edad)
        self.escuela = escuela
        
    def getDatos(self):
        return super().getDatos() + ", escuela: " + self.escuela

    def estudiar(self):
        return self.nombre + " está estudiando"
    
p1 = Persona("Alex", "alonso", 27)

e1 = Estudiante("Juan", "Diaz", 17, "IES Teis")

print(p1.getDatos())

print(e1.getDatos())