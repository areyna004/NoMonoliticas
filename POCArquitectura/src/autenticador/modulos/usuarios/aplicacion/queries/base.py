from autenticador.seedwork.aplicacion.queries import QueryHandler
from autenticador.modulos.usuarios.infraestructura.fabricas import FabricaRepositorio
from autenticador.modulos.usuarios.dominio.fabricas import FabricaUsuario

class UsuariosQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_usuarios: FabricaUsuario = FabricaUsuario()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios