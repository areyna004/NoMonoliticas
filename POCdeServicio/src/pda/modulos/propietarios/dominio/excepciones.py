from pda.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioPropietariosExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de propietarios'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)