def decoradora(aDecorar):
    def decorada(*args, **kwargs):
        print("Voy a realizar una operación")
        aDecorar(*args, **kwargs)
        print("Acabe!!")
    return decorada 

@decoradora
def suma(n1, n2):
    print(n1+n2)

@decoradora
def resta(n1, n2):
    print(n1-n2)

@decoradora
def potencia(base, exponente):
    print(base**exponente)

suma(10,5)
resta(10,5)
potencia(2,5)
potencia(base=2,exponente=5)