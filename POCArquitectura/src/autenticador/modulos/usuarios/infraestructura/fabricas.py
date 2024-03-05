from dataclasses import dataclass, field
from autenticador.seedwork.dominio.fabricas import Fabrica
from autenticador.seedwork.dominio.repositorios import Repositorio
from autenticador.modulos.usuarios.dominio.repositorios import RepositorioUsuarios
from autenticador.modulos.usuarios.dominio.entidades import Usuario
from .repositorios import RepositorioUsuariosSQLite
from .excepciones import ExcepcionFabrica
from uuid import UUID

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioUsuarios.__class__:
            return RepositorioUsuariosSQLite()
        else:
            raise ExcepcionFabrica()
        
  