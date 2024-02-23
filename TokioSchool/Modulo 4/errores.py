if __name__=='__main__':      
    # SyntaxError -> Son los que podemos apreciar repasando el código, no se ejecuta ninguna línea del código
    # NameError -> Se producen cuando quier ejecutar alguna función, método... pero no lo encuentra definido
    # IndexError -> Se producen cuando se intenta acceder a una posición que no existe
    # TypeError o ValueError -> Se producn cuando no se pueden hacer castings

    # Excepciones

    while(True):
        try:
            n = float(input("Introduce un número: "))
            m = 4
            print("{}/{}={}".format(n,m,n/m))
        except:
            print("Ha ocurrido un error, introduce bien el número")
        else:
            print("Todo ha funcionado correctamente")
            break  # Importante romper la iteración si todo ha salido bien
        finally:
            print("Fin de la iteración") # Siempre se ejecuta
    print("Continuamos el programa por aquí ...")

    try:
        n = float(input("Introduce un número: "))
        5/n
    except TypeError:
        print("No se puede dividir el número por una cadena")
    except ValueError:
        print("Debes introducir una cadena que sea un número")
    except ZeroDivisionError:
        print("No se puede dividir por cero, prueba otro número")
    except Exception as e:
        print( type(e).__name__ )