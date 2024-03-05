from modulos.propiedades.dominio.eventos import PropiedadAgregada
from seedwork.aplicacion.handlers import Handler
from modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_propiedad_agregada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')
