sistema_solar = "Mercurio Venus Tierra Marte Marte Júpiter Urano Tierra"

planetas = set(sistema_solar.split(" "))

#for i in sistema_solar.split(" "):
#    planetas.add(i)

print(planetas)
print(len(planetas))

import queue

miCola = queue.Queue()          #FIFO

miCola.put("Madrid")
miCola.put("Bogota")
miCola.put("Vigo")

for elemento in miCola.queue:
    print(elemento)
print("-----------------------")
miCola.get()
for elemento in miCola.queue:
    print(elemento)

miCola = queue.LifoQueue()          #LIFO

miCola.put("Madrid")
miCola.put("Bogota")
miCola.put("Vigo")

for elemento in miCola.queue:
    print(elemento)
print("-----------------------")
miCola.get()
for elemento in miCola.queue:
    print(elemento)

miCola = queue.PriorityQueue()          #Priority

miCola.put((3,"Madrid"))
miCola.put((111,"Bogota"))
miCola.put((2,"Vigo"))

for elemento in miCola.queue:
    print(elemento)
print("-----------------------")
miCola.get()
for elemento in miCola.queue:
    print(elemento)