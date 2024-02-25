from __future__ import annotations

from dataclasses import dataclass, field
from pda.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion
from datetime import datetime
from enum import Enum

class TipoPropiedad(Enum):
    DEPARTAMENTO = "Departamento"
    CASA = "Casa"
    OFICINA = "Oficina"
    TERRENO = "Terreno"

@dataclass(frozen=True)
class NombrePropiedad():
    nombre: str

@dataclass(frozen=True)
class DescripcionPropiedad():
    nombre: str

@dataclass(frozen=True)
class TamanioPropiedad():
    nombre: int