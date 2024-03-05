from seedwork.dominio.repositorios import Mapeador
from modulos.propiedades.dominio.objetos_valor import Direccion
from modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO
from .dto import Direccion as DireccionDTO

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_direccion_dto(self, direcciones_dto: list) -> list[Direccion]:
        direccion_dict = dict()
        
        for dir in direcciones_dto:
            calle = dir.calle
            localidad = dir.localidad
            ciudad = dir.ciudad
            pais = dir.pais
            direccion_dict.setdefault(str(dir.dir_orden), Direccion(calle, localidad, ciudad, pais))
        
        direcciones = list()
        
        for dir_dict in direccion_dict.items():
            direcciones.append(dir_dict)

        return direcciones

    def _procesar_direccion(self, direcciones: any) -> list[DireccionDTO]:
        direcciones_dto = list()
        for k, direccion in enumerate(direcciones):
            direccion_dto = DireccionDTO()
            direccion_dto.calle = direccion.calle
            direccion_dto.localidad = direccion.localidad
            direccion_dto.ciudad = direccion.ciudad
            direccion_dto.pais = direccion.pais
            direccion_dto.dir_orden = k
            direcciones_dto.append(direccion_dto)
        return direcciones_dto

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.fecha_creacion = entidad.fecha_creacion
        propiedad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.nombre = entidad.nombre
        propiedad_dto.descripcion = entidad.descripcion
        propiedad_dto.tamanio = entidad.tamanio
        propiedad_dto.tipo = entidad.tipo
        propiedad_dto.direcciones = self._procesar_direccion(entidad.direcciones)
        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.nombre, dto.descripcion, dto.tamanio, dto.tipo)
        propiedad.direcciones = list()
        direcciones_dto: list[DireccionDTO] = dto.direcciones
        propiedad.direcciones.append(self._procesar_direccion_dto(direcciones_dto))
        return propiedad