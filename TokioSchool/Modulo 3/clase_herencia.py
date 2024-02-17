class Producto():
    def __init__(self,idproducto,nombre,precio,descripcion):
        self.idproducto = idproducto
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        
    def __str__(self):
        return """-> PRODUCTO <-
        - IdProducto: {}
        - Nombre: {}
        - Precio: {}
        - Descripción: {}""".format(self.idproducto,self.nombre,self.precio,self.descripcion)
    
class Alimento(Producto):
    def __init__(self,idproducto,nombre,precio,descripcion,productor,distribuidor):
        super().__init__(idproducto,nombre,precio,descripcion)
        self.productor = productor
        self.distribuidor = distribuidor
        
    def __str__(self):
        return """-> PRODUCTO ALIMENTO <-
        - IdProducto: {}
        - Nombre: {}
        - Precio: {}
        - Descripción: {}
        - Productor: {}
        - Distribuidor: {}""".format(self.idproducto,self.nombre,self.precio,self.descripcion,self.productor,self.distribuidor)
    
class Libro(Producto):
    def __init__(self,idproducto,nombre,precio,descripcion,isbn,autor):
        super().__init__(idproducto,nombre,precio,descripcion)
        self.isbn = isbn
        self.autor = autor
    
    def __str__(self):
        return """-> PRODUCTO LIBRO <-
        - IdProducto: {}
        - Nombre: {}
        - Precio: {}
        - Descripción: {}
        - ISBN: {}
        - Autor: {}""".format(self.idproducto,self.nombre,self.precio,self.descripcion,self.isbn,self.autor)
    
class Ropa(Producto):
    def __init__(self,idproducto,nombre,precio,descripcion,talla,marca):
        super().__init__(idproducto,nombre,precio,descripcion)
        self.talla = talla
        self.marca = marca
    
    def __str__(self):
        return """-> PRODUCTO ROPA <-
        - IdProducto: {}
        - Nombre: {}
        - Precio: {}
        - Descripción: {}
        - Talla: {}
        - Marca: {}""".format(self.idproducto,self.nombre,self.precio,self.descripcion,self.talla,self.marca)
    
if __name__ == "__main__":
    al = Alimento(48975,"Botella de Aceite de Oliva Extra",5,"250 ML","La Aceitera","Distribuciones SA")
    li = Libro(15897,"Cocina Japonesa",15,"Recetas de oriente","1265626526856","Maestro Sun")
    ro = Ropa(11236,"Jersey Fit18",18,"Jersey de hombre de invierno","36","Guci")

    productos = [al, li, ro]
    for p in productos:
        print(p,"\n")
    for p in productos:
        if( isinstance(p, Alimento) ):
            print(p.idproducto, "->", p.nombre, "->", p.productor)
        elif( isinstance(p, Libro) ):
            print(p.idproducto, "->", p.nombre, "->", p.isbn)     
        elif( isinstance(p, Ropa) ):
            print(p.idproducto, "->", p.nombre, "->", p.marca)