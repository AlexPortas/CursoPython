class Vehiculo():
    def __init__(self, color, ruedas, ancho, alto):
        self.color = color
        self.ruedas = ruedas
        self.ancho = ancho
        self.alto = alto
    
    def arrancar(self):
        return "Estoy arrancado"
    
    def acelerar(self):
        return "Estoy acelerando"

    def frenar(self):
        return "Estoy frenando"

    def girar(self):
        return "Estoy girando"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, ancho, alto, carga, cilindrada, marchas, asientos, aire):
        super().__init__(color, ruedas, ancho, alto)
        self.carga = carga
        self.cilindrada = cilindrada
        self.marchas = marchas
        self.asientos = asientos
        self.aire = aire
    
    def cargar(self):
        return "Estoy cargando"
    
    def derrapar(self):
        return "Estoy derrapando"

    def marchaAtras(self):
        return "Estoy llendo marcha atras"


class Furgoneta(Coche):
    def __init__(self, color, ruedas, ancho, alto, carga, cilindrada, marchas, asientos, aire):
        super().__init__(color, ruedas, ancho, alto, carga, cilindrada, marchas, asientos, aire)

class Bici(Vehiculo):
    def __init__(self, color, ruedas, ancho, alto):
        super().__init__(color, ruedas, ancho, alto)
        
    def saltar(self):
        return "Estoy saltando"

class Moto(Bici):
    def __init__(self, color, ruedas, ancho, alto, cilindrada, marchas):
        super().__init__(color, ruedas, ancho, alto)
        self.cilindrada = cilindrada
        self.marchas = marchas
          
    def derrapar(self):
        return "Estoy derrapando"

    def marchaAtras(self):
        return "Estoy llendo marcha atras"
        
