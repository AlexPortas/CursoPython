class Persona():
    __nombre = ""
    __edad = 0
    genero = "sin definir"

    def __init__(self, nombre, genero):
        self.__nombre = nombre
        self.genero = genero

    def setEdad(self,ed):
        if(ed<0 or ed>100):
            print("Error en la edad.")
        else:
            self.__edad = ed
            return self.__edad
            
    def hablar(self):
        return self.__nombre + " está hablando"
    
    def caminar(self):
        return self.__nombre + " está caminando" 
        
    def getDatos(self):
        return "Nombre: " + self.__nombre + ", edad: " + str(self.__edad) + ", género: " + self.genero
    
p1 = Persona("Alex", "masculino")

p1.setEdad(-9)
p1.setEdad(25)
p1.setEdad(1566)

print(p1.getDatos())