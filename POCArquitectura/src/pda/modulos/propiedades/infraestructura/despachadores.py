import pulsar
from pulsar.schema import *

from modulos.propiedades.infraestructura.schema.v1.eventos import PropiedadAgregada, PropiedadAgregadaPayload
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(PropiedadAgregada))
        publicador.send(mensaje)
        cliente.close()
    
    def _publicar_mensaje_comando(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearPropiedad))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadAgregadaPayload(
            id_propiedad=str(evento.id_reserva), 
            id_propietario=str(evento.id_propietario), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = PropiedadAgregada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(PropiedadAgregada))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearPropiedadPayload(
            fecha_creacion  = comando.fecha_creacion,
            fecha_actualizacion = comando.fecha_actualizacion,
            id = comando.id,
            nombre = comando.nombre,
            descripcion = comando.descripcion,
            tamanio = str(comando.tamanio),
            tipo = comando.tipo,
            direcciones = comando.direcciones
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje_comando(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))