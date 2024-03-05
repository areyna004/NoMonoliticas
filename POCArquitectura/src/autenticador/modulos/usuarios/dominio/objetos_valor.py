from __future__ import annotations

from dataclasses import dataclass, field
from autenticador.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class NombreUsuario():
    nombre: str

@dataclass(frozen=True)
class TokenUsuario():
    token: str