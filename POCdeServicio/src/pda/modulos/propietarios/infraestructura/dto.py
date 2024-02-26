from pda.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propietario(db.Model):
    __tablename__ = "propietarios"
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    propiedades = db.Column(db.String, nullable=False)