class CuentaCorriente():
    n_cuenta = ""
    titular = ""
    saldo = 0

    def __init__(self, n_cuenta, titular, saldo):
        self.n_cuenta = str(n_cuenta)
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cant):
        self.saldo += cant
    
    def retirar(self, cant):
        self.saldo -= cant
        
    def getDatos(self):
        return "Nº cuenta: " + self.n_cuenta + ", titular: " + self.titular + ", saldo: " + str(self.saldo)

class CuentaJoven(CuentaCorriente):
    def __init__(self, n_cuenta, titular, saldo, bonus_promocion=0):
        super().__init__(n_cuenta, titular, saldo)
        self.bonus = bonus_promocion
        self.saldo += bonus_promocion
    
    def getBonus(self):
        return "El bonus promocional es de " + str(self.bonus)

    def getDatos(self):
        return super().getDatos() + ", bonus: " + str(self.bonus)


c1 = CuentaCorriente(1234, "masculino", 100)

c1.ingresar(50)

c1.retirar(75)

print(c1.getDatos())

c2 = CuentaJoven("ES12425O134", "Pepe Masculino", 100, 30)

print(c2.getBonus())

c2.ingresar(50)

c2.retirar(75)

print(c2.getDatos())