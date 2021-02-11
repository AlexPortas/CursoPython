def introducirNombres():
    nombres = []
    intentos = 0
    while intentos<3:
        try:
            nombre = input("Introduce un nombre: ")
    
            if nombre in nombres:
                raise ValueError
            else:
                nombres.append(nombre)
        except ValueError:
            print("Error. Este nombre ya se a utilizado. "+nombre)
        finally:
            intentos+=1
    
    return nombres

print(introducirNombres())
    