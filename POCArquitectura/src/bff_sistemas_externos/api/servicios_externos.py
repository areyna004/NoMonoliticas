import json, functools, io
from flask import redirect, render_template, request, session, url_for
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
from pulsar import Client, AuthenticationToken

def crear_blueprint(identificador: str, prefijo_url: str):
    return Blueprint(identificador, __name__, url_prefix=prefijo_url)

propiedad_schema = Parse(open("src/bff_sistemas_externos/api/schema/v1/propiedad.avsc").read())

bp = crear_blueprint('usuarios_externos', '/usuarios_externos')

@bp.route('/propiedad', methods=['POST'])
def agregar_propiedad():
    try:
        propiedad_data = request.json
        bytes_io = io.BytesIO()
        writer = DatumWriter(propiedad_schema)
        encoder = BinaryEncoder(bytes_io)
        writer.write(propiedad_data, encoder)
        encoded_data = bytes_io.getvalue()
        client = Client('pulsar://127.0.0.1:6650')
        producer = client.create_producer('persistent://public/default/comandos-propiedades')   
        producer.send(encoded_data)
        return Response('{}', status=202, mimetype='application/json')
        
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
