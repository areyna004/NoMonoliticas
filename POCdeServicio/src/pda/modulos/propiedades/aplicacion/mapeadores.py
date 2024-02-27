from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap
from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.modulos.propiedades.dominio.objetos_valor import Direccion
from .dto import PropiedadDTO, DireccionDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def _procesar_direcciones(self, direcciones: list[DireccionDTO]):
        direcciones_dto: list[Direccion] = list()

        for direccion in direcciones:
            direccion_dto: DireccionDTO = DireccionDTO(direccion.get('calle'), direccion.get('localidad'), direccion.get('ciudad'), direccion.get('pais'))
            direcciones_dto.append(direccion_dto)

        return direcciones_dto
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        direcciones: list[DireccionDTO] = self._procesar_direcciones(externo.get('direcciones', list()))
        propiedad_dto = PropiedadDTO('','','',externo.get('nombre'), externo.get('descripcion'), externo.get('tamanio'), externo.get('tipo'), direcciones)
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_direcciones(self, direcciones_dto: list[DireccionDTO]):
        direcciones = list()

        for direccion_dto in direcciones_dto:
            nombre: str = direccion_dto.calle
            localidad: str = direccion_dto.localidad
            ciudad: str = direccion_dto.ciudad
            pais: str = direccion_dto.pais
            direccion: Direccion = Direccion(nombre, localidad, ciudad, pais)
            direcciones.append(direccion)

        return direcciones

    def obtener_tipo(self) -> type:
        return Direccion.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        nombre = entidad.nombre
        descripcion = entidad.descripcion
        tamanio = entidad.tamanio
        tipo = entidad.tipo
        eventos = entidad.eventos
        direcciones = entidad.direcciones
        return PropiedadDTO(fecha_creacion, fecha_actualizacion, _id, nombre, descripcion, tamanio, tipo, direcciones)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propiedad.nombre = dto.nombre
        propiedad.descripcion = dto.descripcion
        propiedad.tamanio = dto.tamanio
        propiedad.tipo = dto.tipo
        direcciones_dto: list[DireccionDTO] = dto.direcciones
        propiedad.direcciones = self._procesar_direcciones(direcciones_dto)
        return propiedad