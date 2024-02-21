class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
            
# Vamos a crear un metodo que recibira por parametro un objeto del tipo vehiculo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

# Programa principal, fuera de las clases
if __name__=='__main__':
    print("USO NORMAL (SIN POLIMORFISMO)")
    # Cada objeto instanciado de cada una de las 3 clases accede a su metodo desplazamiento
    miVehiculo = Moto()
    miVehiculo.desplazamiento()

    miVehiculo2 = Coche()
    miVehiculo2.desplazamiento()

    miVehiculo3 = Camion()
    miVehiculo3.desplazamiento()
    
    print("\nUSO DE POLIMORFISMO")
    miVehiculo4 = Camion()
    desplazamientoVehiculo(miVehiculo4)
    miVehiculo5 = Moto()
    desplazamientoVehiculo(miVehiculo5)