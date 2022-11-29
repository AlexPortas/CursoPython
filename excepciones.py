def suma(n1, n2):
    return n1+n2

def resta(n1, n2):
    return n1-n2

def multiplica(n1, n2):
    return n1*n2

def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        return "No se puede dividir por 0"

num1 = 15
num2 = 3



d="alex","coche",32
print(d,type(d))
