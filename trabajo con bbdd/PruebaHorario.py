        
from typing import TextIO


class Usuario():
    def __init__(self, nombre, dictDias):
        self.nombre=nombre
        self.horario={}
        for x, y in dictDias.items():
            self.montar_dia(x, y)
        print("Usuario {} creado".format(self.nombre))
    
    def anhadir_actividad(self, dia, primera_hora, ultima_hora, actividad):
        if primera_hora==ultima_hora:
            self.horario[dia][primera_hora-1].anhadir_a_sesion(actividad)
        else:
            self.horario[dia][primera_hora-1].anhadir_a_sesion(actividad)
            self.horario[dia][primera_hora+1-1].anhadir_a_sesion(actividad)
            self.horario[dia][ultima_hora-1].anhadir_a_sesion(actividad)

    def anhadir_horario(self, dia, hora, traballador):
        self.horario[dia][hora-1].anhadir_a_sesion(traballador)
        
    def quitar_horario(self, dia, hora):
        self.horario[dia][hora-1].quitar_de_la_sesion()

    def montar_dia(self, nombreDia, antesDescanso):
        if antesDescanso==2:
            self.horario[nombreDia]=[Sesion(60), Sesion(60), Sesion(40), Sesion(40), Sesion(40)]
        elif antesDescanso==3:
            self.horario[nombreDia]=[Sesion(40), Sesion(40), Sesion(40), Sesion(40), Sesion(40), Sesion(40)]
        
    def mostrar_horario(self):
        print("Horario de usuario {}".format(self.nombre))
        print("-"*40)
        for dia, horas in self.horario.items():
            print(dia)
            for hora in horas:
                print(Sesion.mostrar_sesion(hora))

    def __str__(self):
        return self.nombre

class Traballador():
    def __init__(self, nombre, dictDias, actividad):
        self.nombre=nombre
        self.actividad=actividad
        self.horario={}
        for x, y in dictDias.items():
            self.montar_dia(x, y)
        print("Traballador {} creado".format(self.nombre))
    
    def anhadir_actividad(self, dia, primera_hora, ultima_hora, actividad):
        self.horario[dia][primera_hora-1].indicar_dia_hora(dia, primera_hora, ultima_hora)
        if primera_hora==ultima_hora:
            self.horario[dia][primera_hora-1].anhadir_a_sesion(actividad,True)
        else:
            self.horario[dia][primera_hora-1].anhadir_a_sesion(actividad,True)
            self.horario[dia][primera_hora+1-1].anhadir_a_sesion(actividad,True)
            self.horario[dia][ultima_hora-1].anhadir_a_sesion(actividad,True)
        
    def anhadir_horario(self, dia, hora, usuario):
        self.horario[dia][hora-1].anhadir_a_sesion(usuario)

    def quitar_horario(self, dia, hora, usuario):
        self.horario[dia][hora-1].quitar_de_la_sesion(usuario)

    def montar_dia(self, nombreDia, antesDescanso):
        if antesDescanso==2:
            self.horario[nombreDia]=[Sesion(60), Sesion(60), Sesion(40), Sesion(40), Sesion(40)]
        elif antesDescanso==3:
            self.horario[nombreDia]=[Sesion(40), Sesion(40), Sesion(40), Sesion(40), Sesion(40), Sesion(40)]
            
    def mostrar_horario(self):
        print("Horario de traballador {}".format(self.nombre))
        print("-"*40)
        for dia, horas in self.horario.items():
            print(dia)
            for hora in horas:
                print(Sesion.mostrar_sesion(hora))
    
    def __str__(self):
        return self.nombre

class Sesion():
    def __init__(self, duracion):
        self.sesionCon = []
        self.duracion=duracion
        self.nombre_actividad=""
    
    def anhadir_a_sesion(self, obj, t=False):
        if type(obj).__name__=="Traballador":
            self.sesionCon.append(obj.nombre)
            self.nombre_actividad=""
        if type(obj).__name__=="Usuario":
            self.sesionCon.append(obj.nombre)
            self.nombre_actividad=obj.actividad
        if type(obj).__name__=="Actividad":
            if t:
                self.sesionCon=obj.usuarios
            else:
                self.sesionCon=obj.traballadores
            self.nombre_actividad=obj.nombre

    def indicar_dia_hora(self, dia, primera_hora, ultima_hora):
        self.dia=dia
        self.primera_hora=primera_hora
        self.ultima_hora=ultima_hora
    
    def quitar_de_la_sesion(self, obj=None):
        if obj.nombre in self.sesionCon:
            if len(self.sesionCon)>1:
                for i,v in enumerate(self.sesionCon):
                    if v==obj.nombre:
                        self.sesionCon.pop(i)
                        break
            else:
                self.sesionCon.pop(0)
        else:
            print("Usuariio {} no encontrado!!".format(obj.nombre))
    
    def mostrar_sesion(self):
        if len(self.sesionCon)>1:
            texto=""
            for i,v in enumerate(self.sesionCon):
                if len(self.sesionCon) == i+1:
                    texto+=str(v)
                else:
                    texto+=str(v)+", "
            return self.nombre_actividad + " -> " + texto
        else:
            return self.nombre_actividad + " -> " + str(self.sesionCon[0])

class Actividad():
    def __init__(self, nombre, traballadores=[], usuarios=[]):
        self.nombre=nombre
        self.traballadores=traballadores
        self.usuarios=usuarios
    
    def mostrar_actividad(self):
        print("--->>>",self.nombre,"<<<---")
        print("Traballadores:")
        for t in self.traballadores:
            print(t.nombre)
        print("Usuarios:")
        for u in self.usuarios:
            print(u.nombre)


def poner_en_horario(u, t, dia, hora):
    u.anhadir_horario(dia, hora,t)
    t.anhadir_horario(dia, hora,u)

def quitar_en_horario(u, t, dia, hora):
    u.quitar_horario(dia, hora)
    t.quitar_horario(dia,hora,u)
    
u1=Usuario("ioshu", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
u2=Usuario("ana", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
u3=Usuario("raquel", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
u4=Usuario("kinn", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
t1=Traballador("sarai", {"lunes":3,"martes":3,"mercores":2,"xoves":2},"Terapia")
t2=Traballador("nuria", {"lunes":3,"martes":3,"mercores":2,"xoves":2},"ES")
t3=Traballador("cris", {"lunes":3,"martes":3,"mercores":2,"xoves":2},"Fisioterapia")
t4=Traballador("marta", {"lunes":3,"martes":3,"mercores":2,"xoves":2},"ES")
g1=[u1,u2]
g2=[u3,u4]
gt1= [t1,t2]
gt2=[t4]
a1a=Actividad("a1a",gt1,g1)
a1b=Actividad("a1b",gt2,g2)
a2a=Actividad("a2a",gt1,g1)
a2b=Actividad("a2b",gt2,g2)
b1a=Actividad("b1a",gt1,g1)
b1b=Actividad("b1b",gt2,g2)
b2a=Actividad("b2a",gt1,g1)
b2b=Actividad("b2b",gt2,g2)
c1a=Actividad("c1a",gt1,g1)
c1b=Actividad("c1b",gt2,g2)
c2a=Actividad("c2a",gt1,g1)
c2b=Actividad("c2b",gt2,g2)
c3a=Actividad("c3a",gt1,g1)
c3b=Actividad("c3b",gt2,g2)
d1a=Actividad("d1a",gt1,g1)
d1b=Actividad("d1b",gt2,g2)
d2a=Actividad("d2a",gt1,g1)
d2b=Actividad("d2b",gt2,g2)
d3a=Actividad("d3a",gt1,g1)
d3b=Actividad("d3b",gt2,g2)
activ=[a1a,a1b,a2a,a2b,b1a,b1b,b2a,b2b,c1a,c1b,c2a,c2b,c3a,c3b,d1a,d1b,d2a,d2b,d3a,d3b]
for a in activ:
        a.mostrar_actividad()
u1.anhadir_actividad("lunes",1,3,a1a)
u1.anhadir_actividad("lunes",4,6,a2b)
t1.anhadir_actividad("lunes",1,3,a1a)
t1.anhadir_actividad("lunes",4,6,a2b)
u1.anhadir_actividad("martes",1,3,b2a)
u1.anhadir_actividad("martes",4,6,b2b)
t1.anhadir_actividad("martes",1,3,b2a)
t1.anhadir_actividad("martes",4,6,b2b)
u1.anhadir_actividad("mercores",1,1,c1a)
u1.anhadir_actividad("mercores",2,2,c2b)
u1.anhadir_actividad("mercores",3,5,c3a)
t1.anhadir_actividad("mercores",1,1,c1b)
t1.anhadir_actividad("mercores",2,2,c2a)
t1.anhadir_actividad("mercores",3,5,c3b)
u1.anhadir_actividad("xoves",1,1,d1a)
u1.anhadir_actividad("xoves",2,2,d2b)
u1.anhadir_actividad("xoves",3,5,d3a)
t1.anhadir_actividad("xoves",1,1,d1b)
t1.anhadir_actividad("xoves",2,2,d2a)
t1.anhadir_actividad("xoves",3,5,d3b)
u1.mostrar_horario()
t1.mostrar_horario()
'''
# meter datox

poner_en_horario(u1,t1,"lunes",1)
poner_en_horario(u1,t1,"lunes",2)
poner_en_horario(u1,t2,"lunes",3)
poner_en_horario(u1,t2,"lunes",4)
poner_en_horario(u1,t3,"lunes",5)

poner_en_horario(u2,t1,"lunes",1)
poner_en_horario(u2,t2,"lunes",2)
poner_en_horario(u2,t3,"lunes",4)
poner_en_horario(u2,t3,"lunes",5)
poner_en_horario(u2,t1,"lunes",6)

poner_en_horario(u3,t3,"lunes",1)
poner_en_horario(u3,t3,"lunes",2)
poner_en_horario(u3,t1,"lunes",3)
poner_en_horario(u3,t1,"lunes",4)
poner_en_horario(u3,t2,"lunes",6)
               
u1.mostrar_horario()
u2.mostrar_horario()
u3.mostrar_horario()
t1.mostrar_horario()
t2.mostrar_horario()
t3.mostrar_horario()

quitar_en_horario(u2,t3,"lunes",4)
quitar_en_horario(u2,t3,"lunes",5)
quitar_en_horario(u2,t3,"lunes",5)
quitar_en_horario(u2,t3,"lunes",6)
quitar_en_horario(u1,t1,"lunes",1)
'''
