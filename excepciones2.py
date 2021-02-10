def divide():
    try:
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la operación es "+str(n1/n2))
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("Valor introducido incorrecto")

divide()