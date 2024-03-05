from config.db import Base, engine, SessionLocal
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, String, DateTime, ForeignKeyConstraint

import uuid

propiedades_direcciones = Table(
    "propiedades_direcciones",
    Base.metadata,
    Column("propiedad_id", String, ForeignKey("propiedades.id")),
    Column("dir_orden", Integer),
    Column("calle", String),
    Column("localidad", String),
    Column("ciudad", String),
    Column("pais", String),
    ForeignKeyConstraint(
        ["dir_orden", "calle", "localidad", "ciudad", "pais"],
        ["direcciones.dir_orden", "direcciones.calle", "direcciones.localidad", "direcciones.ciudad", "direcciones.pais"]
    )
)

class Direccion(Base):
    __tablename__ = "direcciones"
    dir_orden = Column(Integer, nullable=False)
    calle = Column(String, primary_key=True, nullable=False)
    localidad = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)

class Propiedad(Base):
    __tablename__ = "propiedades"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    fecha_creacion = Column(DateTime, nullable=False)
    fecha_actualizacion = Column(DateTime, nullable=False)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    tamanio = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    direcciones = relationship('Direccion', secondary=propiedades_direcciones, backref='propiedades')