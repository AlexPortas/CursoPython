from sqlalchemy import true


calcula_cubo = lambda num,exponente: num**exponente

print(calcula_cubo(10, 5))

comission_formato = lambda comision:"¡{}€!".format(comision)

print(comission_formato(3200))

lista = [(5, 20), (6, 2), (1, 10), (55, 5)]

lista.sort(key=lambda t: t[0]+t[1])

print(lista)