import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
    
# De aquí para bajo es mío
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    planetas = relationship("PlanetaFav", back_populates="usuario")
    personajes = relationship("PersonajeFav", back_populates="usuario")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer)
    users = relationship("PlanetaFav", back_populates="planeta")

class PlanetaFav(Base):
    __tablename__ = 'planetafav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    users = relationship("Usuario", back_populates="planetas")
    planet_id = Column(Integer, ForeignKey('planeta.id'))
    planets = relationship("Planeta", back_populates="users")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    origin = Column(String, ForeignKey('planeta.name'))
    usuarios = relationship("PersonajeFav", back_populates="personaje")
    faction_id = Column(Integer, ForeignKey('faction.id'))
    faction = relationship('Faction', back_populates='personajes')

class PersonajeFav(Base):
    __tablename__ = 'personajefav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    users = relationship("Usuario", back_populates="personajes")
    char_id = Column(Integer, ForeignKey('personaje.id'))
    characters = relationship("Personaje", back_populates="usuarios")

class Faction(Base):
    __tablename__ = 'faction'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    personajes = relationship('Personaje', back_populates='faction')
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
