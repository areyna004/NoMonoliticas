from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap
from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.modulos.propiedades.dominio.objetos_valor import Propietario
from .dto import PropiedadDTO, PropietarioDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def _procesar_propietario(self, propietario: dict) -> PropietarioDTO:
        propietario_dto: PropietarioDTO = PropietarioDTO(propietario.get('nombre'), propietario.get('direccion'), propietario.get('tipo'))
        return PropietarioDTO(propietario_dto)
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propietario: PropietarioDTO = externo.get('propietario')
        self._procesar_propietario(propietario)
        propiedad_dto = PropiedadDTO = PropiedadDTO(externo.get('nombre'), externo.get('descripcion'), externo.get('tamanio'), externo.get('tipo'), externo.get('direccion'), self._procesar_propiedad(propietario))
        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_propietario(self, propietario_dto: PropietarioDTO) -> Propietario:
        nombre: str = propietario_dto.get('nombre')
        direccion: str = propietario_dto.get('direccion')
        tipo: str = propietario_dto.get('tipo')
        propietario: Propietario = Propietario(nombre, direccion, tipo)
        return Propietario(propietario)

    def obtener_tipo(self) -> type:
        return Propietario.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        nombre: entidad.nombre
        descripcion: entidad.descripcion
        tamanio: entidad.tamanio
        tipo: entidad.tipo
        direccion: entidad.direccion
        return PropiedadDTO(fecha_creacion, fecha_actualizacion, _id, nombre, descripcion, tamanio, tipo, direccion, list())

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        propietario_dto: PropietarioDTO = self._procesar_itinerario(dto.itinerarios)   
        propiedad.propietario = propietario_dto    
        return propiedad