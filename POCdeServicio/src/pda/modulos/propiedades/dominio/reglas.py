from pda.seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Ruta
from .entidades import Pasajero
from .objetos_valor import TipoPasajero, Itinerario


class TamanioMayorAMetro(ReglaNegocio):

    tamanio: int

    def __init__(self, tamanio, mensaje='El tamaño de la propiedad debe ser mayor a un metro'):
        super().__init__(mensaje)
        self.tamanio = tamanio

    def es_valido(self) -> bool:
        if self.tamanio >= 1:
            return True
        else:
            return False

