import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

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

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    tarrain = Column(String(250))
    usrface_water = Column(String(250))
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    homeworld_id = Column(Integer, ForeignKey('planet.id'),nullable=False)
    homeworld = relationship(Planet)
    mass = Column(String(250))
    skin_color = Column(String(250))
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    
class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(= Column(String(250))(250))
    episode_id int
    opening_crawl = Column(String(250))
    director = Column(String(250))
    producer = Column(String(250))
    release_date date
    species array
    starships array
    vehicles array
    characters array
    planets array
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class PeopleFilm(Base):
    __tablename__ = 'peopleFilm'
    people_id pk FK >- People.id
    film_id pk FK >- Films.id


class PeopleVehicle(Base):
    __tablename__ = 'peoplevehicle'
    people_id int PK FK >- People.id
    vehicle_id int PK FK >- Vehicles.id

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    lenght = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    pilots array
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    tarrain = Column(String(250))
    usrface_water = Column(String(250))
    residents array
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class Specie(Base):
    __tablename__ = 'specie'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(String(250))
    average_lifespan = Column(String(250))
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    language = Column(String(250))
    homeworld_id int
    people array
    url = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))

class PlanetFilm(Base):
    __tablename__ = 'planetfilm'
    planet_id pk int FK >- Planets.id
    film_id pk int FK >- Films.id

class VehicleFilm(Base):
    __tablename__ = 'vehiclefilm'
    vehicle_id pk int FK >- Vehicles.id
    film_id pk int FK >- Films.id

class SpeciePlanet(Base):
    __tablename__ = 'specieplanet'
    specie_id pk int FK >- Species.id
    planet_id pk int FK >- Planets.id

class PeopleSpecie(Base):
    __tablename__ = 'peoplebase'
    specie_id pk int FK >- Species.id
    people_id pk int FK >- People.id

class SpecieFilm(Base):
    __tablename__ = 'speciefilm'
    specie_id pk int FK >- Species.id
    film_idpk int FK >- Films.id

class SpecieVehicle(Base):
    __tablename__ = 'specievehicle'
    specie_id pk int FK >- Species.id
    vehicle_id pk int FK >- Vehicles.id




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')