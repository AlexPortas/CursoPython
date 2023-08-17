import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table

'''
ONE TO MANY (1:N)
 -> 1 Articulo puede tener N (muchos) Comentarios
 -> 1 Comentario pertenece a 1 Articulo
'''

class Articulo(db.Base):
    __tablename__ = 'articulo'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    # La clase débil simplemente indica que tiene una relación con Comentario
    #relacion_comentario = relationship("Comentario")

    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return "Articulo({}: {})".format(self.id, self.titulo)


class Comentario(db.Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    texto = Column(String)
    # La clase fuerte de la relación (el lado de la N) recibe la PK del lado débil y es la que indica que hay una relación
    id_articulo = Column(Integer, ForeignKey('articulo.id'))
    articulo = relationship(Articulo, uselist=False, backref="articulo_al_que_pertenece")

    def __init__(self, texto, articulo):
        self.texto = texto
        self.articulo = articulo

    def __str__(self):
        return "Comentario({}: {})".format(self.id, self.texto)


'''
ONE TO ONE (1:1)
 -> 1 Persona puede tener 1 Móvil de empresa
 -> 1 Móvil de empresa pertenece a 1 Persona
'''

class Persona(db.Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    movil = relationship("Movil", uselist=False, backref="propietario")
    '''
    Pasamos dos parámetros adicionales a la función de relación. 
     -> uselist=False, hace que SQLAlchemy comprenda que Movil contendrá solo una única instancia y no una matriz (múltiple) de instancias. 
     -> backref, es una referencia al objeto del otro lado de la asignación.
    '''

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Persona({}: {} -> {})".format(self.id, self.nombre, self.movil)

class Movil(db.Base):
    __tablename__ = "movil"
    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    persona = Column(Integer, ForeignKey('persona.id'))

    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return "Móvil({}: {} -> {})".format(self.id, self.numero, self.persona)

'''
ONE TO MANY (N:N)
 -> 1 Estudiante puede tener N (muchas) Clases
 -> 1 Clase puede tener N (muchos) Estudiantes
'''

estudiantes_clases_asociacion = Table('estudiantes_clases', db.Base.metadata,
    Column('estudiante_id', Integer, ForeignKey('estudiante.id')),
    Column('clase_id', Integer, ForeignKey('clase.id'))
)

class Estudiante(db.Base):
    __tablename__ = 'estudiante'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Estudiante({}: {})".format(self.id, self.nombre)

class Clase(db.Base):
    __tablename__ = 'clase'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    estudiantes = relationship("Estudiante", secondary=estudiantes_clases_asociacion)

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Clase({}: {})".format(self.id, self.nombre)