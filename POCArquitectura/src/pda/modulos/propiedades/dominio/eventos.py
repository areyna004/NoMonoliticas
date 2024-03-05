from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class PropiedadAgregada(EventoDominio):
    id_propiedad: uuid.UUID = None
    nombre: uuid.UUID = None
    fecha_creacion: datetime = None
    