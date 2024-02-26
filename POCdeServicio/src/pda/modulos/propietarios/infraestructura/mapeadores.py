from pda.seedwork.dominio.repositorios import Mapeador
from pda.modulos.propietarios.dominio.entidades import Propietario
from .dto import Propietario as PropietarioDTO

class MapeadorPropietario(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propietario.__class__

    def entidad_a_dto(self, entidad: Propietario) -> PropietarioDTO:
        propietario_dto = PropietarioDTO()
        propietario_dto.fecha_creacion = entidad.fecha_creacion
        propietario_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propietario_dto.id = str(entidad.id)
        propietario_dto.nombre = entidad.nombre
        propietario_dto.propiedades = entidad.propiedades
        return propietario_dto

    def dto_a_entidad(self, dto: PropietarioDTO) -> Propietario:
        propietario = Propietario(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.nombre, dto.propiedades)
        return propietario