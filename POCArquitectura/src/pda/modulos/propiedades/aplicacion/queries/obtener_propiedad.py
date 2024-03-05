from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
import uuid

@dataclass
class ObtenerPropiedad(Query):
    id: str

class ObtenerPropiedadHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        reserva =  self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_reserva(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)