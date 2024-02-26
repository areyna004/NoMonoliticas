from dataclasses import dataclass, field
from pda.seedwork.dominio.fabricas import Fabrica
from pda.seedwork.dominio.repositorios import Repositorio
from pda.modulos.propietarios.dominio.repositorios import RepositorioPropietarios
from .repositorios import RepositorioPropietariosSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropietarios.__class__:
            return RepositorioPropietariosSQLite()
        else:
            raise ExcepcionFabrica()