from pda.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

propiedades_direcciones = db.Table(
    "propiedades_direcciones",
    db.Model.metadata,
    db.Column("propiedad_id", db.String, db.ForeignKey("propiedades.id")),
    db.Column("dir_orden", db.Integer),
    db.Column("calle", db.String),
    db.Column("localidad", db.String),
    db.Column("ciudad", db.String),
    db.Column("pais", db.String),
    db.ForeignKeyConstraint(
        ["dir_orden", "calle", "localidad", "ciudad", "pais"],
        ["direcciones.dir_orden", "direcciones.calle", "direcciones.localidad", "direcciones.ciudad", "direcciones.pais"]
    )
)
class Direccion(db.Model):
    __tablename__ = "direcciones"
    dir_orden = db.Column(db.Integer,nullable=False)
    calle = db.Column(db.String, primary_key=True, nullable=False)
    localidad = db.Column(db.String,nullable=False)
    ciudad = db.Column(db.String,nullable=False)
    pais = db.Column(db.String,nullable=False)

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    tamanio = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    direcciones = db.relationship('Direccion', secondary=propiedades_direcciones, backref='propiedades')