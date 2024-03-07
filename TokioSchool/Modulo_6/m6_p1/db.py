from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#engine
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread':False})

#sesion
Session = sessionmaker(bind=engine)
sesion = Session()

#vinculacion
Base = declarative_base()