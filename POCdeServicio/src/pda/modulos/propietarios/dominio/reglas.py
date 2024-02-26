from pda.seedwork.dominio.reglas import ReglaNegocio
from .entidades import Propietario

class MasDeUnaPropiedad(ReglaNegocio):
    propietario: Propietario
    
    def __init__(self, propietario, mensaje='Debe tener al menos una propiedad'):
        super().__init__(mensaje)
        self.propietario = propietario

    def es_valido(self) -> bool:
        #print(self.propiedad)
        if self.propietario.propiedades != " ":
            return True
        else:
            return False

