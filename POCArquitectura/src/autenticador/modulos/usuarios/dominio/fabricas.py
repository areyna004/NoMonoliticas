from .entidades import Usuario
from .excepciones import TipoObjetoNoExisteEnDominioUsuariosExcepcion
from autenticador.seedwork.dominio.repositorios import Mapeador, Repositorio
from autenticador.seedwork.dominio.fabricas import Fabrica
from autenticador.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaUsuario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            usuario: Usuario = mapeador.dto_a_entidad(obj)
            return usuario

@dataclass
class FabricaUsuario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Usuario.__class__:
            fabrica_usuario = _FabricaUsuario()
            return fabrica_usuario.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioUsuariosExcepcion()