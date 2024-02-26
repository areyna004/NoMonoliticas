from pda.seedwork.aplicacion.servicios import Servicio
from pda.modulos.propietarios.dominio.entidades import Propietario
from pda.modulos.propietarios.dominio.fabricas import FabricaPropietario
from pda.modulos.propietarios.infraestructura.fabricas import FabricaRepositorio
from pda.modulos.propietarios.infraestructura.repositorios import RepositorioPropietarios
from .mapeadores import MapeadorPropietario

from .dto import PropietarioDTO

class ServicioPropietario(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propietarios: FabricaPropietario = FabricaPropietario()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propietarios(self):
        return self._fabrica_propietarios

    def crear_propietario(self, propietario_dto: PropietarioDTO) -> PropietarioDTO:
        propietario: Propietario = self.fabrica_propietarios.crear_objeto(propietario_dto, MapeadorPropietario())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropietarios.__class__)
        repositorio.agregar(propietario)
        return self.fabrica_propietarios.crear_objeto(propietario, MapeadorPropietario())

    def obtener_propietario_por_id(self, id) -> PropietarioDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropietarios.__class__)
        return repositorio.obtener_por_id(id).__dict__
    
    def obtener_todas_los_propietarios(self) -> list[PropietarioDTO]:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropietarios.__class__)
        propietarios = repositorio.obtener_todos()
        mapeador = MapeadorPropietario()
        propietarios_dto = [mapeador.entidad_a_dto(propietario) for propietario in propietarios]
        return propietarios_dto
    