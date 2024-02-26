from pda.config.db import db
from pda.modulos.propietarios.dominio.repositorios import RepositorioPropietarios
from pda.modulos.propietarios.dominio.entidades import Propietario
from pda.modulos.propietarios.dominio.fabricas import FabricaPropietario
from .dto import Propietario as PropietarioDTO
from .mapeadores import MapeadorPropietario
from uuid import UUID

class RepositorioPropietariosSQLite(RepositorioPropietarios):

    def __init__(self):
        self._fabrica_propietarios: FabricaPropietario = FabricaPropietario()

    @property
    def fabrica_propietarios(self):
        return self._fabrica_propietarios

    def obtener_por_id(self, id: UUID) -> Propietario:
        propietario_dto = db.session.query(PropietarioDTO).filter_by(id=str(id)).first()
        return self.fabrica_propietarios.crear_objeto(propietario_dto, MapeadorPropietario())

    def obtener_todos(self) -> list[Propietario]:
        propietarios_dto = db.session.query(PropietarioDTO).all()
        propietarios: list[PropietarioDTO]=list()
            
        for propietario in propietarios_dto:    
            propietarios.append(self.fabrica_propietarios.crear_objeto(propietario, MapeadorPropietario()))

        return propietarios
    
    def agregar(self, propietario: Propietario):
        propietario_dto = self.fabrica_propietarios.crear_objeto(propietario, MapeadorPropietario())
        db.session.add(propietario_dto)
        db.session.commit()

    def actualizar(self, reserva: Propietario):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError