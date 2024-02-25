from pda.seedwork.aplicacion.dto import Mapeador as AppMap
from pda.seedwork.dominio.repositorios import Mapeador as RepMap
from pda.modulos.propiedades.dominio.entidades import Reserva, Aeropuerto
from pda.modulos.propiedades.dominio.objetos_valor import Itinerario, Odo, Segmento, Leg
from .dto import PropiedadDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, propiedad: dict) -> PropiedadDTO:
        propiedad_dto: PropiedadDTO = PropiedadDTO(propiedad.get('nombre'), propiedad.get('descripcion'), propiedad.get('tamanio'), propiedad.get('tipo'))
        return PropiedadDTO(propiedad_dto)