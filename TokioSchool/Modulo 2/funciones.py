# funciones

def saluda():
    print("Que pasa contigo, ", nombre, "!!",sep="")
    
def tabla(n=2):
    print('------------ Tabla del', n, '-----------------')
    for i in range(1,11):
        print(n, 'x', i, '=', n*i)

def doblar(numero):
    return numero*2

def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterminado es",t)
    for k in kwargs:
        print(k," ", kwargs[k])

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
        
def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num

if __name__ == "__main__":
    nombre = "Alex"
    saluda()
    tabla()
    tabla(6)
    print(doblar(10))
    super_funcion(10,50,-1,1.56,10,20,300,nombre="Hector",edad=27)
    cuenta_atras(5)
    print(factorial(10))