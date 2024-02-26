from pda.config.db import db
from pda.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from pda.modulos.propiedades.dominio.objetos_valor import TipoPropiedad
from pda.modulos.propiedades.dominio.entidades import Propiedad
from pda.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID

class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).first()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        propiedades_dto = db.session.query(PropiedadDTO).all()
        propiedades: list[PropiedadDTO]=list()
            
        for propiedad in propiedades_dto:    
            propiedades.append(self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad()))

        return propiedades
    
    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)
        db.session.commit()

    def actualizar(self, reserva: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError