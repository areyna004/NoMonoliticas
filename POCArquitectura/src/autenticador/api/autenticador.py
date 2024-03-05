import autenticador.seedwork.presentacion.api as api
import json
from autenticador.seedwork.dominio.excepciones import ExcepcionDominio
from autenticador.seedwork.aplicacion.queries import ejecutar_query
from autenticador.modulos.usuarios.aplicacion.queries.revisar_token import RevisarToken

from flask import redirect, render_template, request, session, url_for
from flask import Response

bp = api.crear_blueprint('autenticador', '/autenticador')

@bp.route('/usuario', methods=['GET'])
def revisar_token():
    try:
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            partes = authorization_header.split()
            if len(partes) == 2 and partes[0] == 'Bearer':
                token = partes[1]
                query_resultado = ejecutar_query(RevisarToken(token))
                if query_resultado.resultado == True: 
                    return f'Token de autorización: {token}', 200
                else:
                    return 'Token no autorizado', 403
            else:
                return 'Token de autorización mal formado', 400
        else:
            return 'Token de autorización no proporcionado', 401
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')