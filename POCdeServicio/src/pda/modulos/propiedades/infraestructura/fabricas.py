from dataclasses import dataclass, field
from pda.seedwork.dominio.fabricas import Fabrica
from pda.seedwork.dominio.repositorios import Repositorio
from pda.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioPropiedadesSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesSQLite()
        else:
            raise ExcepcionFabrica()