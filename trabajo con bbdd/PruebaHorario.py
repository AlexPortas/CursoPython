        
class Usuario():
    def __init__(self, nombre, dictDias):
        self.nombre=nombre
        self.horario={}
        for x, y in dictDias.items():
            self.montar_dia(x, y)
        print("Usuario {} creado".format(self.nombre))
    
    def anhadir_horario(self, dia, hora, traballador):
        self.horario[dia][hora-1]=traballador.actividad
        
    def quitar_horario(self, dia, hora):
        self.horario[dia][hora-1]="libre"

    def montar_dia(self, nombreDia, antesDescanso):
        if antesDescanso==2:
            self.horario[nombreDia]=[Sesion(60, type(self).__name__), Sesion(60, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__)]
        elif antesDescanso==3:
            self.horario[nombreDia]=[Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__)]
        
    def mostrar_horario(self):
        print("Horario de usuario {}".format(self.nombre))
        print("-"*40)
        for dia, horas in self.horario.items():
            print(dia,"->", horas)

class Traballador():
    def __init__(self, nombre, dictDias, actividad):
        self.nombre=nombre
        self.actividad=actividad
        self.horario={}
        for x, y in dictDias.items():
            self.montar_dia(x, y)
        print("Traballador {} creado".format(self.nombre))
    
    def anhadir_horario(self, dia, hora, usuario):
        self.horario[dia][hora-1].append(usuario.nombre)

    def quitar_horario(self, dia, hora, usuario):
        if usuario.nombre in self.horario[dia][hora-1]:
            if len(self.horario[dia][hora-1])>1:
                for i,v in enumerate(self.horario[dia][hora-1]):
                    if v==usuario.nombre:
                        self.horario[dia][hora-1].pop(i)
                        break
            else:
                self.horario[dia][hora-1].pop(0)
        else:
            print("Usuariio {} no encontrado en la {} hora del dia {}".format(usuario.nombre, hora, dia))
    
    def montar_dia(self, nombreDia, antesDescanso):
        if antesDescanso==2:
            self.horario[nombreDia]=[Sesion(60, type(self).__name__), Sesion(60, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__)]
        elif antesDescanso==3:
            self.horario[nombreDia]=[Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__), Sesion(40, type(self).__name__)]
            
    def mostrar_horario(self):
        print("Horario de traballador {}".format(self.nombre))
        print("-"*40)
        for dia, horas in self.horario.items():
            print(dia,"->", horas)

class Sesion():
    def __init__(self, duracion, tObj):
        if tObj=="Traballador":
            self.sesionCon = []
        if tObj=="Usuario":
            self.sesionCon = "libre"
        self.duracion=duracion
    

    
    def __str__(self):
        return str(self.sesionCon)

def poner_en_horario(u, t, dia, hora):
    u.anhadir_horario(dia, hora,t)
    t.anhadir_horario(dia, hora,u)

def quitar_en_horario(u, t, dia, hora):
    u.quitar_horario(dia, hora)
    t.quitar_horario(dia,hora,u)
    
u1=Usuario("ioshu", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
u2=Usuario("ana", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
u3=Usuario("raquel", {"lunes":3,"martes":3,"mercores":2,"xoves":2})
t1=Traballador("sarai", {"lunes":3,"martes":3,"mercores":2,"xoves":2},"Terapia")
t2=Traballador("nuria", {"lunes":3,"martes":3,"mercores":2,"xoves":2},"ES")
t3=Traballador("iria", {"lunes":3,"martes":3,"mercores":2},"Psico")

# meter datox
'''
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
   '''              
u1.mostrar_horario()
u2.mostrar_horario()
u3.mostrar_horario()
t1.mostrar_horario()
t2.mostrar_horario()
t3.mostrar_horario()
'''
quitar_en_horario(u2,t3,4)
quitar_en_horario(u2,t3,5)
quitar_en_horario(u2,t3,5)
quitar_en_horario(u2,t3,6)
quitar_en_horario(u1,t1,1)
t3.mostrar_horario()
u1.mostrar_horario()'''
