from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap
from pda.modulos.propietarios.dominio.entidades import Propietario
from pda.modulos.propietarios.dominio.objetos_valor import Direccion
from .dto import PropietarioDTO

from datetime import datetime
import json

class MapeadorPropietarioDTOJson(AppMap):  
    def externo_a_dto(self, externo: dict) -> PropietarioDTO:
        propietario_dto = PropietarioDTO()
        propietario_dto = PropietarioDTO('','','',externo.get('nombre'), externo.get('propiedades'))
        return propietario_dto

    def dto_a_externo(self, dto: PropietarioDTO) -> dict:
        return dto.__dict__

class MapeadorPropietario(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propietario.__class__

    def entidad_a_dto(self, entidad: Propietario) -> PropietarioDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        nombre = entidad.nombre
        propiedades = entidad.propiedades
        return PropietarioDTO(fecha_creacion, fecha_actualizacion, _id, nombre, propiedades)

    def dto_a_entidad(self, dto: PropietarioDTO) -> Propietario:
        propietario = Propietario()
        propietario.nombre = dto.nombre
        propietario.propiedades = json.dumps(dto.propiedades)
        return propietario