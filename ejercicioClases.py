class Cuenta():
    n_cuenta = ""
    titular = ""
    saldo = 0

    def __init__(self, n_cuenta, titular, saldo):
        self.n_cuenta = str(n_cuenta)
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cant):
        self.saldo += cant
        return "Se ha ingresado " + str(cant) + " €"
    
    def retirar(self, cant):
        self.saldo -= cant
        return "Se ha retirado " +str(cant) + " €"
        
    def getDatos(self):
        return "Nº cuenta: " + self.n_cuenta + ", titular: " + self.titular + ", saldo: " + str(self.saldo)
    
p1 = Cuenta(1234, "masculino", 100)

p1.ingresar(50)

p1.retirar(75)

print(p1.getDatos())