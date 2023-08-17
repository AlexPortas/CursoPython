from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# El engine permite a SQLAlchemy comunicarse con la base de datos
# https://docs.sqlalchemy.org/en/14/core/engines.html
engine = create_engine('sqlite:///M6_sqlalchemy_v2/database/personas.db')
# Advertencia, crear el engine no conecta inmediantamente a la base de datos, es lo hacemos más adelante

# Ahora creamos la sesión, lo que nos permite realizar transacciones (operaciones) dentro de nuestra DB
Session = sessionmaker(bind=engine)
session = Session()

# Ahora vamos al fichero models.py y creamos nuestro modelo (nuestra clase) y la siguiente instrucción
# se encarga de mapear la clase o clases creadas y vincularlas a la base de datos
Base = declarative_base()