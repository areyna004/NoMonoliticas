import json, functools, io
from flask import redirect, render_template, request, session, url_for
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
from pulsar import Client, AuthenticationToken
from bff_sistemas_externos.api.utils import revisar_token

class OrderSaga:
    def __init__(self):
        ...

    def autenticar_usuario(self, propiedad_json, token):
        is_token = revisar_token(token)
        if is_token == None:
            raise Exception("No se pudo autenticar el usuario")

    def step2(self, propiedad_json, token):
        print("Step 2: Perform action 2 for order")

    def step3(self, propiedad_json, token):
        print("Step 3: Perform action 3 for order")

    def compensate_step2(self, propiedad_json, token):
        print("Compensating Step 2 for order")

    def compensate_step3(self, propiedad_json, token):
        print("Compensating Step 3 for order")

    def execute(self, propiedad_json, token):
        self.propiedad_json = propiedad_json
        try:
            self.autenticar_usuario(self.propiedad_json, token)
            self.step2(self.propiedad_json, token)
            self.step3(self.propiedad_json, token)
        except Exception as e:
            print('exception')
            self.compensate_step3(self.propiedad_json, token)
            self.compensate_step2(self.propiedad_json, token)
            raise e



'''bytes_io = io.BytesIO()
            writer = DatumWriter(propiedad_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(propiedad_data, encoder)
            encoded_data = bytes_io.getvalue()  
            client = Client('pulsar://10.182.0.2:6650')
            producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
            producer_comandos_propiedad.send(encoded_data)
            client.close()'''


