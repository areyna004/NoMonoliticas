from pda.seedwork.aplicacion.comandos import Comando
from pda.modulos.propiedades.aplicacion.dto import PropiedadDTO, DireccionDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from pda.seedwork.aplicacion.comandos import ejecutar_commando as comando

from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from pda.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from pda.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades

@dataclass
class CrearPropiedad(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str
    descripcion: str
    tamanio: str
    tipo: str
    direcciones: str


class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   nombre=comando.id
            ,   descripcion=comando.id
            ,   tamanio=comando.id
            ,   tipo=comando.id
            ,   direcciones=comando.direcciones)

        propiedad: Propiedad = self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)