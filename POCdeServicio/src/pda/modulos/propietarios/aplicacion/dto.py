from dataclasses import dataclass, field
from pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropietarioDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    propiedades: str = field(default_factory=str)
