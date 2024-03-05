from __future__ import annotations
from dataclasses import dataclass, field

import autenticador.modulos.usuarios.dominio.objetos_valor as ov
from autenticador.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Usuario(AgregacionRaiz):
    nombre: ov.NombreUsuario = field(default_factory=ov.NombreUsuario)
    token: ov.TokenUsuario = field(default_factory=ov.TokenUsuario)