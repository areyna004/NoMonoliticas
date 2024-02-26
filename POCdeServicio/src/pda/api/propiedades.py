import pda.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response

from pda.seedwork.dominio.excepciones import ExcepcionDominio
from pda.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from pda.modulos.propiedades.aplicacion.servicios import ServicioPropiedad

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/propiedad', methods=['POST'])
def agregar_propiedad():
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        sr = ServicioPropiedad()
        dto_final = sr.crear_propiedad(propiedad_dto)
        return map_propiedad.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/propiedad', methods=['GET'])
@bp.route('/propiedad/<id>', methods=['GET'])
def dar_propiedad(id=None):
    if id:
        sr = ServicioPropiedad()
        return sr.obtener_propiedad_por_id(id)
    
    else:
        sr = ServicioPropiedad()
        return sr.obtener_todas_las_propiedades()