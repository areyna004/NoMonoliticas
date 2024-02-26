from .entidades import Propietario
from .reglas import MasDeUnaPropiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropietariosExcepcion
from pda.seedwork.dominio.repositorios import Mapeador, Repositorio
from pda.seedwork.dominio.fabricas import Fabrica
from pda.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPropietario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            self.validar_regla(MasDeUnaPropiedad(obj))
            return mapeador.entidad_a_dto(obj)
            
        else:
            propietario: Propietario = mapeador.dto_a_entidad(obj)
            return propietario

@dataclass
class FabricaPropietario(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propietario.__class__:
            fabrica_propietario = _FabricaPropietario()
            return fabrica_propietario.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropietariosExcepcion()