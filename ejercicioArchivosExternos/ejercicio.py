import io
import os

os.chdir('ejercicioArchivosExternos')

f = io.open('clientes.txt', 'r', encoding='UTF-8')

listaClientes = f.readlines()

f.close()

clientes = []

for cliente in listaClientes:
    campo = cliente.split(';')
    cliente = {"Codigo":campo[0], "Nombre":campo[1], "Direccion":campo[2], "Poblacion":campo[3], "Telefono":campo[4], "Responsable":campo[5]}
    clientes.append(cliente)

for c in clientes:
    print("Código Articulo={} Nombre={} Dirección={} Población={} Tfno={} Responsable={}".format(c['Codigo'],c['Nombre'], c['Direccion'], c['Poblacion'], c['Telefono'], c['Responsable']))