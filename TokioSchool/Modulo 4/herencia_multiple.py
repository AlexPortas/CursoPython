class Vehiculos():         
    def __str__(self):
        return Vehiculos.__str__(self) + "\n" + VElectricos.__str__(self)
    # Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print("Creado objeto de la clase Vehiculos")
        
    def __str__(self):
        return "Marca: {}\nModelo: {}".format(self.marca,self.modelo)

class VElectricos():
    
    # Constructor
    def __init__(self, autonomia):
        self.autonomia = autonomia
        print("Creado objeto de la clase VElectricos")
        
    def __str__(self):
        return "Autonomia: {}".format(self.autonomia)
        
class BicicletaElectrica(VElectricos,Vehiculos):
    '''Clase BicicletaElectrica que hereda de la clase Vehiculos y de la clase VElectricos, es decir, herencia multiple'''
    
    def __init__(self, marca=None, modelo=None, autonomia=None):
        VElectricos.__init__(self, autonomia) # Equivalente a: super().__init__(autonomia)
        Vehiculos.__init__(self, marca, modelo)
        print("Creado objeto de la clase BicicletaElectrica")
    
    def __str__(self):
        return Vehiculos.__str__(self) + "\n" + VElectricos.__str__(self)
        # Equivalente a return Vehiculos.__str__(self) + "\n" + super().__str__()

if __name__=='__main__':
    miBici = BicicletaElectrica("Ford", "Xtreme", 80)
    print(miBici, end="\n\n")
    miBici2 = BicicletaElectrica("Ford", "Xtreme")
    print(miBici2, end="\n\n")
    miBici3 = BicicletaElectrica("Ford", None, 100)
    print(miBici3)