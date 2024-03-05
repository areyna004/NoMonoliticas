from __future__ import annotations
from dataclasses import dataclass, field

import modulos.propiedades.dominio.objetos_valor as ov
from modulos.propiedades.dominio.eventos import PropiedadAgregada
from seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Propiedad(AgregacionRaiz):
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    tamanio: int = field(default_factory=int)
    tipo: str = field(default_factory=str)
    direcciones: list[ov.Direccion] = field(default_factory=ov.Direccion)

    def crear_propiedad(self, propiedad: Propiedad):
        self.nombre = propiedad.nombre
        self.descripcion = propiedad.descripcion
        self.tamanio = propiedad.tamanio
        self.tipo = propiedad.tipo
        self.direcciones = propiedad.direcciones
        self.agregar_evento(PropiedadAgregada(id_reserva=self.id, fecha_creacion=self.fecha_creacion))
