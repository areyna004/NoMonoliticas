import json, functools, io
from flask import redirect, render_template, request, session, url_for
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
from pulsar import Client, AuthenticationToken
from bff_sistemas_externos.api.utils import revisar_token

def crear_blueprint(identificador: str, prefijo_url: str):
    return Blueprint(identificador, __name__, url_prefix=prefijo_url)

propiedad_schema = Parse(open("src/bff_sistemas_externos/api/schema/v1/propiedad.avsc").read())

client = Client('pulsar://34.16.163.13:6650')

consumer_comandos_propiedades = client.subscribe('persistent://public/default/eventos-propiedades', 'subscripcion-bff')
producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades') 
producer_consultas_propiedad = client.create_producer('persistent://public/default/consultas-propiedades') 

bp = crear_blueprint('usuarios_externos', '/usuarios_externos')

@bp.route('/propiedad', methods=['POST'])
def agregar_propiedad():
    try:
        token = revisar_token()
        if token:
            propiedad_data = request.json
            bytes_io = io.BytesIO()
            writer = DatumWriter(propiedad_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(propiedad_data, encoder)
            encoded_data = bytes_io.getvalue()  
            producer_comandos_propiedad.send(encoded_data)
            return Response('{}', status=202, mimetype='application/json')
        else:
            return Response('Unauthorized', status=403, mimetype='application/json')
        
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedad', methods=['GET'])
def detalle_propiedad():
    try:
        token = revisar_token()
        if token:
            propiedad_data = request.json
            bytes_io = io.BytesIO()
            writer = DatumWriter(propiedad_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(propiedad_data, encoder)
            encoded_data = bytes_io.getvalue()
            producer_consultas_propiedad.send(encoded_data)

            return Response('{}', status=202, mimetype='application/json')
        else:
            return Response('Unauthorized', status=403, mimetype='application/json')
        
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')