class Pelicula():
    def __init__(self,titulo,duracion,lanzamiento, director):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.director = director
        print("Se ha creado la película",self.titulo)
        
    def __del__(self):
        print("Se ha borrando la película", self.titulo)
        
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos -> {}".format(self.titulo,self.lanzamiento,self.duracion, self.director)
                  
class Director():
    def __init__(self, nombre, apellido, edad="desconocida"):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print("Se ha creado el director {} {} con una edad {}".format(self.nombre, self.apellido, self.edad))
        
    def __str__(self):
        return "Director {} {} con edad {}".format(self.nombre, self.apellido, self.edad)
    
class Catalogo():
    peliculas = []      
    
    def __init__(self,peliculas=[]):
        self.peliculas = peliculas
        if(len(self.peliculas) == 0):
            print('Se ha creado el catalogo vacío')
        else:
            print('Se ha creado el catalogo con las peliculas asignadas')
        
    def agregar(self,p):  
        self.peliculas.append(p)
        print('Se ha agregado al catalogo la película: {}'.format(p.titulo))
        
    def mostrar(self):
        for p in self.peliculas:
            print(p) 

if __name__ == "__main__":
    d1 = Director("Ridley", "Scott", 84)
    d2 = Director("George", "Lucas")
    p1 = Pelicula("El Padrino",175,1972,d2)
    p2 = Pelicula("Alien el octavo pasajero", 200, 1979, d1)
    print(p1.__dict__)
    print(p1)
    del p1
    p1 = Pelicula("El Padrino",175,1972,d2)
    c = Catalogo()
    c.agregar(p1)
    c.agregar(p2)
    c.mostrar()
    print(c)