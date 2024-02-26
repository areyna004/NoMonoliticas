import pda.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response

from pda.seedwork.dominio.excepciones import ExcepcionDominio
from pda.modulos.propietarios.aplicacion.mapeadores import MapeadorPropietarioDTOJson
from pda.modulos.propietarios.aplicacion.servicios import ServicioPropietario

bp = api.crear_blueprint('propietarios', '/propietarios')

@bp.route('/propietario', methods=['POST'])
def agregar_propietario():
    try:
        propietario_dict = request.json
        map_propietario = MapeadorPropietarioDTOJson()
        propietario_dto = map_propietario.externo_a_dto(propietario_dict)
        sr = ServicioPropietario()
        dto_final = sr.crear_propietario(propietario_dto)
        return map_propietario.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/propietario', methods=['GET'])
@bp.route('/propietario/<id>', methods=['GET'])
def dar_propietario(id=None):
    if id:
        sr = ServicioPropietario()
        return sr.obtener_propietario_por_id(id)
    
    else:
        sr = ServicioPropietario()
        return sr.obtener_todas_los_propietarios()