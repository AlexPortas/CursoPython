from sqlalchemy import Column, String, Boolean, Integer
import db


class Tarea(db.Base):
    __tablename__="tarea"
    __table_args__={"sqlite_autoincrement": True}
    id_tarea=Column(Integer, primary_key=True)
    contenido=Column(String(100), nullable=False)
    completado=Column(Boolean)

    def __init__(self, contenido, completado):
        self.contenido=contenido
        self.completado=completado

    def __str__(self):
        if self.completado:
            return "Tarea {}: {} - Tarea realizada".format(self.id_tarea, self.contenido)
        else:
            return "Tarea {}: {} - Tarea pendiente ".format(self.id_tarea, self.contenido)