from dataclasses import dataclass, field
from pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropietarioDTO(DTO):
    nombre: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    tipo: str = field(default_factory=str)

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    tamanio: int = field(default_factory=int)
    tipo: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    propietario: PropietarioDTO

