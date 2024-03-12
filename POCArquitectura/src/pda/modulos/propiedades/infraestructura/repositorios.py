from config.db import SessionLocal, Base, engine, init_db
from modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from modulos.propiedades.dominio.objetos_valor import TipoPropiedad
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.dominio.fabricas import FabricaPropiedades
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
        engine, SessionLocal, Base = init_db()
        session = SessionLocal()
        propiedad_dto = session.query(PropiedadDTO).filter_by(id=str(id)).first()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        engine, SessionLocal, Base = init_db()
        session = SessionLocal()
        propiedades_dto = session.query(PropiedadDTO).all()
        propiedades: list[PropiedadDTO]=list()
            
        for propiedad in propiedades_dto:    
            propiedades.append(self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad()))

        return propiedades
    
    def agregar(self, propiedad: Propiedad):
        engine, SessionLocal, Base = init_db()
        session = SessionLocal()
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
        session.add(propiedad_dto)
        session.commit()

    def actualizar(self, reserva: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad: Propiedad):
        engine, SessionLocal, Base = init_db()
        session = SessionLocal()
        propiedad_dto = session.query(PropiedadDTO).filter_by(nombre=str(propiedad.nombre)).first()
        print('aqui *********************************')
        session.delete(propiedad_dto)
        session.commit()