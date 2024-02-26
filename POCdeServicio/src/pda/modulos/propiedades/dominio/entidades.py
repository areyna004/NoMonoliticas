from __future__ import annotations
from dataclasses import dataclass, field

import pda.modulos.propiedades.dominio.objetos_valor as ov
from pda.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Propiedad(AgregacionRaiz):
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    tamanio: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    direcciones: list[ov.Direccion] = field(default_factory=ov.Direccion)