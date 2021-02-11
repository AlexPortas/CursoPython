def introducirNombres():
    nombres = []
    intentos = 0
    while intentos<3:
        nombre = input("Introduce un nombre: ")
    
        if nombre in nombres:
            raise ValueError("Error. Este nombre ya se a utilizado.")
        else:
            nombres.append(nombre)
    
        intentos+=1
    
    return nombres

print(introducirNombres())
    