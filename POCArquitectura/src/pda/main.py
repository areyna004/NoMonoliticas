from pulsar import Client, AuthenticationToken
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
import mysql.connector
import io, json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from seedwork.dominio.excepciones import ExcepcionDominio
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from seedwork.aplicacion.queries import ejecutar_query
from seedwork.aplicacion.comandos import ejecutar_commando
from modulos.propiedades.infraestructura.despachadores import Despachador

from config.db import init_db

comando_schema = Parse(open("src/notificaciones/schema/v1/propiedad-comando.avsc").read())
evento_schema = Parse(open("src/notificaciones/schema/v1/propiedad-evento.avsc").read())

def consumir_comandos():
    client = Client('pulsar://127.0.0.1:6650')
    consumer = client.subscribe('persistent://public/default/comandos-propiedades', 'subscripcion-2')
    producer = client.create_producer('persistent://public/default/eventos-propiedades')
    while True:
        try:
            msg = consumer.receive()
            bytes_io = io.BytesIO(msg.data())
            decoder = BinaryDecoder(bytes_io)
            reader = DatumReader(comando_schema)
            propiedad_externo = reader.read(decoder)
            map_propiedad = MapeadorPropiedadDTOJson()
            propiedad_dto = map_propiedad.externo_a_dto(propiedad_externo)
            sr = ServicioPropiedad()
            dto_final = sr.crear_propiedad(propiedad_dto)
            bytes_io = io.BytesIO()
            writer = DatumWriter(evento_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(dto_final, encoder)
            encoded_data = bytes_io.getvalue()
            producer.send(encoded_data)
            consumer.acknowledge(msg)
        except Exception as e:
            print("Error al procesar el comando:", e)
            consumer.negative_acknowledge(msg)

if __name__ == "__main__":
    engine, SessionLocal, Base = init_db()

    while True:
        consumir_comandos()
        pass
