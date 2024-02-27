from pulsar.schema import *
from pda.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadAgregadaPayload(Record):
    id_propiedad = String()
    id_propietario = String()
    estado = String()
    fecha_creacion = Long()

class PropiedadAgregada(EventoIntegracion):
    data = PropiedadAgregadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)