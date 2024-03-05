from seedwork.dominio.reglas import ReglaNegocio
from .entidades import Propiedad

class TamanioMayorAMetro(ReglaNegocio):
    propiedad: Propiedad
    
    def __init__(self, propiedad, mensaje='El tamaño de la propiedad debe ser mayor a un metro'):
        super().__init__(mensaje)
        self.propiedad = propiedad

    def es_valido(self) -> bool:
        
        if int(str(self.propiedad.tamanio)) >= 1:
            return True
        else:
            return False

