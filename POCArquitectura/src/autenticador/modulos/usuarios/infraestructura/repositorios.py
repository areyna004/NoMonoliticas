from autenticador.config.db import db
from autenticador.modulos.usuarios.dominio.repositorios import RepositorioUsuarios
from autenticador.modulos.usuarios.dominio.objetos_valor import NombreUsuario, TokenUsuario
from autenticador.modulos.usuarios.dominio.entidades import Usuario
from autenticador.modulos.usuarios.dominio.fabricas import FabricaUsuario
from .dto import Usuario as UsuarioDTO
from .mapeadores import MapeadorUsuario
from uuid import UUID

class RepositorioUsuariosSQLite(RepositorioUsuarios):

    def __init__(self):
        self._fabrica_usuarios: FabricaUsuario = FabricaUsuario()

    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios

    def obtener_por_token(self, token: str) -> Usuario:
        usuario_dto = db.session.query(UsuarioDTO).filter_by(token=str(token)).one()
        return self.fabrica_usuarios.crear_objeto(usuario_dto, MapeadorUsuario())
    
    def obtener_por_id(self, id: UUID) -> Usuario:
        # TODO
        raise NotImplementedError
    
    def agregar(self, entity: Usuario):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Usuario):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
    def obtener_todos(self) -> list[Usuario]:
        # TODO
        raise NotImplementedError