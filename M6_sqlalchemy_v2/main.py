import db
import sys
from models import Persona, Articulo, Comentario, Movil, Estudiante, Clase


def relacion_1_N():

    a1 = Articulo(titulo="Python es fantástico")
    a2 = Articulo(titulo="Aliens en Marte.....")
    c1 = Comentario(texto="mola", articulo=a1)
    c2 = Comentario(texto="No se Rick... parece falso...", articulo=a2)
    c3 = Comentario(texto="R por siempre!", articulo=a1)
    db.session.add_all([a1, a2, c1, c2, c3])
    db.session.commit()

    query = db.session.query(Articulo, Comentario).join(Comentario).order_by(Articulo.id).all()
    for a, c in query:
        print("\t > Articulo(ID: {} -> Titulo: {}) \t-> Comentario(ID: {} -> Texto: {})".format(a.id,
                                                                                                a.titulo,
                                                                                                c.id,
                                                                                                c.texto))

    db.session.close()

def relacion_1_N_check():
    articulo2 = (db.session.query(Articulo).filter_by(id=2).first())
    print("\t > ", articulo2)
    comentario1 = (db.session.query(Comentario).filter_by(id=1).first())
    print("\t > ", comentario1)

    comentario1.articulo = articulo2
    db.session.commit()
    print("\t > Añadimos el comentario 1 (que pertenece al articulo 1) al articulo 2, haciendo que un comentario pertenezca a 2 articulos...")

    query = db.session.query(Articulo, Comentario).join(Comentario).order_by(Articulo.id).all()
    for a, c in query:
        print("\t > Articulo(ID: {} -> Titulo: {}) \t-> Comentario(ID: {} -> Texto: {})".format(a.id,
                                                                                                a.titulo,
                                                                                                c.id,
                                                                                                c.texto))
    db.session.close()

    print("\t > Observamos que efectivamente el un comentario no puede pertenecer a 2 articulos a la vez, así que el comentario 1 se queda únicamente en 1 articulo (en el último asignado)")

def relacion_1_1():
    p1 = Persona(nombre="Cristian")
    p2 = Persona(nombre="María")
    p3 = Persona(nombre="Sara")
    m1 = Movil(numero="654789652")
    m2 = Movil(numero="632523698")
    m3 = Movil(numero="658741896")
    p1.movil = m1
    m1.propierario = p1
    p2.movil = m2
    m2.propietario = p2
    p3.movil = m3
    m3.propietario = p3

    db.session.add_all([p1, p2, p3, m1, m2, m3])
    db.session.commit()

    query = db.session.query(Persona, Movil).join(Movil).order_by(Persona.id).all()
    for p, m in query:
        print("\t > Persona(ID: {} -> Nombre: {}) \t-> Móvil(ID: {} -> Número: {})".format(p.id,
                                                                                         p.nombre,
                                                                                         m.id,
                                                                                         m.numero))
    db.session.close()

def relacion_1_1_check():
    movil3 = (db.session.query(Movil).filter_by(id=3).first())
    print("\t > ", movil3)
    persona1 = (db.session.query(Persona).filter_by(id=1).first())
    print("\t > ", persona1)

    movil3.propietario = persona1
    db.session.commit()
    print("\t > Cambiamos el propietario del movil 3, cambiamos a la persona 3 por la persona 1")

    query = db.session.query(Persona, Movil).join(Movil).order_by(Persona.id).all()
    for p, m in query:
        print("\t > Persona(ID: {} -> Nombre: {}) \t-> Móvil(ID: {} -> Número: {})".format(p.id,
                                                                                           p.nombre,
                                                                                           m.id,
                                                                                           m.numero))
    db.session.close()

    print("\t > Observamos que efectivamente el móvil 3 ahora tiene al propietario 1, pero el móvil 1 se ha quedado sin propietario (y por eso no sale, se puede comprobar en la bbdd)")

def relacion_N_N():
    s1 = Estudiante(nombre="Carlos")
    s2 = Estudiante(nombre="Ana")
    c1 = Clase(nombre="Matematicas")
    c2 = Clase(nombre="Historia")
    c1.estudiantes.append(s1)
    c1.estudiantes.append(s2)
    c2.estudiantes.append(s1)
    c2.estudiantes.append(s2)
    db.session.add_all([c1, c2])
    db.session.commit()

    query = db.session.query(Clase).join((Estudiante, Clase.estudiantes)).order_by(Clase.id).all()
    for c in query:
        print("\t > Clase(ID: {} -> Nombre: {})".format(c.id, c.nombre))
        for e in c.estudiantes:
            print("\t\t > Estudiante(ID: {} -> Nombre: {})".format(e.id, e.nombre))

    db.session.close()

if __name__ == '__main__':
    # Reseteamos la base de datos si existe
    db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    #  En la siguiente linea estamos indicando a SQLAlchemy que cree, si no existen, las tablas de
    #  todos los modelos que encuentre en la aplicación. Sin embargo, para que esto ocurra es necesario
    #  que cualquier modelo se haya importado previamente antes de llamar a la función create_all().
    db.Base.metadata.create_all(db.engine)

    while (True):
        print("\n1. Relación 1:N -> Articulo:Comentario\n"
              "2. Comprobar Relación 1:N -> Articulo:Comentario\n"
              "3. Relación 1:1 -> Persona:Movil\n"
              "4. Comprobar Relación 1:1 -> Persona:Movil\n"
              "5. Relación N:N -> Estudiante:Clase\n"
              "6. Salir")
        opcion = int(input("Introduzca una opcion: "))
        if opcion == 1:
            relacion_1_N()
        elif opcion == 2:
            relacion_1_N_check()
        elif opcion == 3:
            relacion_1_1()
        elif opcion == 4:
            relacion_1_1_check()
        elif opcion == 5:
            relacion_N_N()
        elif opcion == 6:
            sys.exit(1)
        else:
            print("Opcion no válida")
