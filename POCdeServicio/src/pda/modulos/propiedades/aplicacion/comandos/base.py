from pda.seedwork.aplicacion.comandos import ComandoHandler
from pda.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from pda.modulos.propiedades.dominio.fabricas import FabricaPropiedades

class CrearPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_propiedades  