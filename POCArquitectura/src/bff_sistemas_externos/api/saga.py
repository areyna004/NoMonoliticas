import json, functools, io, time
from flask import redirect, render_template, request, session, url_for
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
from pulsar import Client, AuthenticationToken
from bff_sistemas_externos.api.utils import revisar_token

class OrderSaga:
    def __init__(self):
        self.propiedad_schema = Parse(open("src/bff_sistemas_externos/api/schema/v1/propiedad.avsc").read())
        self.client = Client('pulsar://10.182.0.2:6650')

    def autenticar_usuario(self, propiedad_json, token):
        is_token = revisar_token(token)
        if is_token == False:
            raise Exception("No se pudo autenticar el usuario")

    def procesar_propiedad(self, propiedad_json, token):
        propiedad_json['accion'] = 'crear'
        bytes_io = io.BytesIO()
        writer = DatumWriter(self.propiedad_schema)
        encoder = BinaryEncoder(bytes_io)
        writer.write(propiedad_json, encoder)
        encoded_data = bytes_io.getvalue()  
        producer_comandos_propiedad = self.client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
        producer_comandos_propiedad.send(encoded_data)

    def comprobar_evento(self, propiedad_json, token):
        consumer = self.client.subscribe('persistent://public/default/eventos-notificaciones', 'notificaciones-subscription-bff')
        start_time = time.time()
        timeout = 1
        while time.time() - start_time < timeout:
            msg = consumer.receive()
            if msg:
                consumer.acknowledge(msg)
                return  
        

    def compensar(self, propiedad_json, token):
        propiedad_json['accion'] = 'eliminar'
        bytes_io = io.BytesIO()
        writer = DatumWriter(self.propiedad_schema)
        encoder = BinaryEncoder(bytes_io)
        writer.write(propiedad_json, encoder)
        encoded_data = bytes_io.getvalue()  
        client = Client('pulsar://10.182.0.2:6650')
        producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
        producer_comandos_propiedad.send(encoded_data)

    def execute(self, propiedad_json, token):
        self.propiedad_json = propiedad_json
        try:
            self.autenticar_usuario(self.propiedad_json, token)
            self.procesar_propiedad(self.propiedad_json, token)
            self.comprobar_evento(self.propiedad_json, token)
            self.client.close()
            return propiedad_json
        except Exception as e:
            self.compensar(self.propiedad_json, token)
            self.client.close()
            return e



'''bytes_io = io.BytesIO()
            writer = DatumWriter(propiedad_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(propiedad_data, encoder)
            encoded_data = bytes_io.getvalue()  
            client = Client('pulsar://10.182.0.2:6650')
            producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
            producer_comandos_propiedad.send(encoded_data)
            client.close()'''


