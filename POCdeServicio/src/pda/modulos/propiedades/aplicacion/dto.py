from dataclasses import dataclass, field
from pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    nombre: str
    descripcion: str
    tamanio: int
    tipo: str