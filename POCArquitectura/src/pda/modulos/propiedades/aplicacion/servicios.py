from seedwork.aplicacion.servicios import Servicio
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.dominio.fabricas import FabricaPropiedades
from modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO

class ServicioPropiedad(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.agregar(propiedad)
        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
    
    def eliminar_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        repositorio.eliminar(propiedad)
        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())

    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return repositorio.obtener_por_id(id).__dict__
    
    def obtener_todas_las_propiedades(self) -> list[PropiedadDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedades = repositorio.obtener_todos()
        mapeador = MapeadorPropiedad()
        propiedades_dto = [mapeador.entidad_a_dto(propiedad) for propiedad in propiedades]
        return propiedades_dto
    