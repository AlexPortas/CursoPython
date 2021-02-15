class Persona():
    nombre = ""
    edad = 0
    genero = "sin definir"

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def hablar(self):
        return self.nombre + " está hablando"
    
    def caminar(self):
        return self.nombre + " está caminando"
        
    def getDatos(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad) + ", género: " + self.genero
    
p1 = Persona("Alex", 27, "masculino")

print(p1.getDatos())