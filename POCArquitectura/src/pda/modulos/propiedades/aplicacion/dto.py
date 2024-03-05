from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO
import json

@dataclass(frozen=True)
class DireccionDTO(DTO):
    calle: str = field(default_factory=str)
    localidad: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    pais: str = field(default_factory=str)

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    tamanio: int = field(default_factory=int)
    tipo: str = field(default_factory=str)
    direcciones: list[DireccionDTO] = field(default_factory=list)

    def to_dict(self):
        return {
            'nombre' : self.nombre
        }

    def to_json(self):
        return json.dumps({
            'nombre' : str(self.nombre)
        })

@dataclass(frozen=True)
class EventoDTO(DTO):
    nombre: str = field(default_factory=str)