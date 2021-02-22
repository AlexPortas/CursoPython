class Persona():
    def hablar(self):
        return "hablo como una persona"

class Trabajador(Persona):
    def hablar(self):
        return "hablo como un trabajador"

class Director(Trabajador):
    def hablar(self):
        return "hablo como un director"

def hazlesHablar(personas):
    for persona in personas:
        print(persona.hablar())

p1 = Persona()
t1 = Trabajador()
d1 = Director()

print(p1.hablar())
print(t1.hablar())
print(d1.hablar())
print("---------------------------")
listaPersonas=[p1, t1, d1]
hazlesHablar(listaPersonas)