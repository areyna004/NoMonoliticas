from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion

from pda.modulos.propiedades.dominio.eventos import PropiedadAgregada 

dispatcher.connect(HandlerReservaIntegracion.handle_propiedad_agregada, signal=f'{PropiedadAgregada.__name__}Integracion')
