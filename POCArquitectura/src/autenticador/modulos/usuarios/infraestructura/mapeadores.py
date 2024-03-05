from autenticador.seedwork.dominio.repositorios import Mapeador
from autenticador.modulos.usuarios.dominio.objetos_valor import NombreUsuario, TokenUsuario
from autenticador.modulos.usuarios.dominio.entidades import Usuario
from .dto import Usuario as UsuarioDTO

class MapeadorUsuario(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Usuario.__class__

    def entidad_a_dto(self, entidad: Usuario) -> UsuarioDTO:
        usuario_dto = UsuarioDTO()
        usuario_dto.fecha_creacion = entidad.fecha_creacion
        usuario_dto.fecha_actualizacion = entidad.fecha_actualizacion
        usuario_dto.id = str(entidad.id)
        usuario_dto.nombre = entidad.nombre
        usuario_dto.token = entidad.token
        return usuario_dto

    def dto_a_entidad(self, dto: UsuarioDTO) -> Usuario:
        usuario = Usuario(dto.id, dto.fecha_creacion, '', dto.fecha_actualizacion, dto.nombre, dto.token)
        return usuario