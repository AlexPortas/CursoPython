class Pelicula():
    def __init__(self,titulo,duracion,lanzamiento, director):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__lanzamiento = lanzamiento
        self.__director = director
        print("Se ha creado la película",self.__titulo)
        
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo): 
        self.__titulo = nuevo

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, nuevo): 
        self.__duracion = nuevo
    
    @property
    def lanzamiento(self):
        return self.__lanzamiento

    @lanzamiento.setter
    def lanzamiento(self, nuevo): 
        self.__lanzamiento = nuevo
    
    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, nuevo): 
        self.__director = nuevo
        
    def __del__(self):
        print("Se ha borrando la película", self.__titulo)
        
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos -> {}".format(self.__titulo,self.__lanzamiento,self.__duracion, self.__director)
                  
class Director():
    def __init__(self, nombre, apellido, edad="desconocida"):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        print("Se ha creado el director {} {} con una edad {}".format(self.__nombre, self.__apellido, self.__edad))
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo): 
        self.__nombre = nuevo
 
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo): 
        self.__apellido = nuevo
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nuevo): 
        self.__edad = nuevo

    def __str__(self):
        return "Director {} {} con edad {}".format(self.__nombre, self.__apellido, self.__edad)
    
class Catalogo():
    def __init__(self,peliculas=[]):
        self.__peliculas = peliculas
        if(len(self.peliculas) == 0):
            print('Se ha creado el catalogo vacío')
        else:
            print('Se ha creado el catalogo con las peliculas asignadas')
        
    @property
    def peliculas(self):
        return self.__peliculas

    @peliculas.setter
    def peliculas(self, nuevo): 
        self.__peliculas = nuevo

    def agregar(self,p):  
        self.peliculas.append(p)
        print('Se ha agregado al catalogo la película: {}'.format(p.titulo))
        
    def mostrar(self):
        for p in self.__peliculas:
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