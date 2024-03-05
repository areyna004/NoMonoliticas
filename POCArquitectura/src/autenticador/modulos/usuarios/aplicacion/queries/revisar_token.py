from autenticador.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from autenticador.seedwork.aplicacion.queries import ejecutar_query as query
from autenticador.modulos.usuarios.infraestructura.repositorios import RepositorioUsuarios
from dataclasses import dataclass
from .base import UsuariosQueryBaseHandler
from autenticador.modulos.usuarios.aplicacion.mapeadores import MapeadorUsuario
import uuid

@dataclass
class RevisarToken(Query):
    token: str

class RevisarTokenHandler(UsuariosQueryBaseHandler):

    def handle(self, query: RevisarToken) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)
        usuario =  self.fabrica_usuarios.crear_objeto(repositorio.obtener_por_token(query.token), MapeadorUsuario())
        auth = False
        if usuario:
            auth = True
        return QueryResultado(resultado=auth)

@query.register(RevisarToken)
def ejecutar_query_obtener_reserva(query: RevisarToken):
    handler = RevisarTokenHandler()
    return handler.handle(query)