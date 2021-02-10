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

operacion = input("Introduce la opwearión a realizar: (+, -, *, /)")

if operacion == "+":
    print(suma(num1,num2))
elif operacion == "-":
    print(resta(num1,num2))
elif operacion == "*":
    print(multiplica(num1,num2))
elif operacion == "/":
    print(divide(num1,num2))
else:
    print("Operación no encontrada")
