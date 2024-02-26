from __future__ import annotations
from dataclasses import dataclass, field

from pda.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Propietario(AgregacionRaiz):
    nombre: str = field(default_factory=str)
    propiedades: list[str] = field(default_factory=list)