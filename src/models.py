import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    name_planetas_id = Column(Integer, ForeignKey('planetas.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
   


class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    heigth = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
   

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    heigth = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)
    passwordr = Column(String(250), nullable=False)
   



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')