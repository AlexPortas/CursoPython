def evaluarUser(user):
    if len(user)>15:
        return "El usuario no puede tener más de 15 caracteres"
    elif len(user)<5:
        return "El usuario no puede tener menos de 5 caracteres"
    if not user.isalnum():
        return "El usuario solo puede contener letras y/o números"
    return True

def evaluarPwd(pwd):
    espacio = False
    minus = False
    mayus = False
    for letra in pwd:
        if letra.isspace():
            espacio = True
        if letra.islower():
            minus = True
        if letra.isupper():
            mayus = True
    if len(pwd)<6:
        return "La contraseña debe tener más de 6 caracteres"
    if pwd.isalnum():
        return "La contraseña debe contener algún carácter especial"
    if not(minus and mayus):
        return "La contraseña no es segura"
    if espacio:
        return "La contraseña no puede contener espacios en blanco"
    return True