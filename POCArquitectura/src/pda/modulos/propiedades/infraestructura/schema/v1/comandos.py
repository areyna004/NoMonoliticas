from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    fecha_creacion  = String()
    fecha_actualizacion = String()
    id = String()
    nombre = String()
    descripcion = String()
    tamanio = String()
    tipo = String()
    direcciones = list()
    

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()