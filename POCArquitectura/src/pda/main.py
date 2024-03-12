from pulsar import Client, Message
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
from modulos.propiedades.aplicacion.dto import EventoDTO

from config.db import init_db

comando_schema = Parse(open("src/pda/schema/v1/propiedad.avsc").read())
evento_schema = Parse(open("src/pda/schema/v1/propiedad.avsc").read())

def consumir_comandos():
    client = Client('pulsar://10.182.0.2:6650')
    consumer = client.subscribe('persistent://public/default/comandos-propiedades', 'subscripcion-2')
    producer = client.create_producer('persistent://public/default/eventos-propiedades')
    producer2 = client.create_producer('persistent://public/default/compensacion-propiedades')
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
            if propiedad_externo['accion'] == 'crear':
                dto_final = sr.crear_propiedad(msg)
                producer.send(dto_final.to_json().encode('utf-8'))
            if propiedad_externo['accion'] == 'eliminar': 
                
                dto_final = sr.eliminar_propiedad(msg)
                producer2.send(dto_final.to_json().encode('utf-8'))
            consumer.acknowledge(msg)
            
        except Exception as e:
            print("Error al procesar el comando:", e)
            consumer.negative_acknowledge(msg)

if __name__ == "__main__":
    engine, SessionLocal, Base = init_db()

    while True:
        consumir_comandos()
