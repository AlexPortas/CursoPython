class Coche():
    ruedas = 4
    largoChasis = 269
    anchoChasis = 130
    arrancado = False

    def arrancar(self):
        self.arrancado = True 

    def estadoCoche(self):
        if (self.arrancado):
            return "El coche está encendido"
        else:
            return "El coche está apagado" 
ford = Coche()

mazda = Coche()

ford.arrancar()

print(ford.estadoCoche())

print(mazda.estadoCoche())