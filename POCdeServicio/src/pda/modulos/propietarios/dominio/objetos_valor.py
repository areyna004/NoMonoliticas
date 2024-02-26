from __future__ import annotations

from dataclasses import dataclass, field
from pda.seedwork.dominio.objetos_valor import ObjetoValor, Locacion
from datetime import datetime
from enum import Enum

class TipoPropiedad(Enum):
    DEPARTAMENTO = "Departamento"
    CASA = "Casa"
    OFICINA = "Oficina"
    TERRENO = "Terreno"

@dataclass(frozen=True)
class Direccion(ObjetoValor):
    calle: str = field(default_factory=str)
    localidad: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    pais: str = field(default_factory=str)

    def calle(self) -> str:
        return self.calle

    def localidad(self) -> str:
        return self.localidad

    def ciudad(self) -> str:
        return self.ciudad
    
    def pais(self) -> str:
        return self.pais