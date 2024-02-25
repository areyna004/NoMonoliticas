from __future__ import annotations
from dataclasses import dataclass, field

import pda.modulos.propiedades.dominio.objetos_valor as ov
from pda.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Propiedad(Entidad):
    tipo: ov.TipoPropiedad = field(default_factory=ov.TipoPropiedad)
    nombre: ov.NombrePropiedad = field(default_factory=ov.NombrePropiedad)
    descripcion: ov.DescripcionPropiedad = field(default_factory=ov.DescripcionPropiedad)
    tamanio: ov.TamanioPropiedad = field(default_factory=ov.TamanioPropiedad)
