from .entidades import Propiedad
from .reglas import TamanioMayorAMetro
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from seedwork.dominio.repositorios import Mapeador, Repositorio
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
            
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)
            print(propiedad)
            #self.validar_regla(TamanioMayorAMetro(propiedad))
            return propiedad

@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_reserva = _FabricaPropiedad()
            return fabrica_reserva.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()