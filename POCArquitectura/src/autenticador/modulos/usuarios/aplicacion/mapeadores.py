from autenticador.seedwork.aplicacion.dto import Mapeador as AppMap
from autenticador.seedwork.dominio.repositorios import Mapeador as RepMap
from autenticador.modulos.usuarios.dominio.entidades import Usuario
from .dto import UsuarioDTO

class MapeadorUsuario(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Usuario.__class__    

    def entidad_a_dto(self, entidad: Usuario) -> UsuarioDTO:
        fecha_creacion = entidad.fecha_creacion
        fecha_actualizacion = entidad.fecha_actualizacion
        _id = str(entidad.id)
        nombre = entidad.nombre
        token = entidad.token
        return UsuarioDTO(fecha_creacion, fecha_actualizacion, _id, nombre, token)

    def dto_a_entidad(self, dto: UsuarioDTO) -> Usuario:
        usuario = Usuario()
        return usuario