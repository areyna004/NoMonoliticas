import pda.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response

from pda.seedwork.dominio.excepciones import ExcepcionDominio
from pda.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from pda.modulos.propiedades.aplicacion.servicios import ServicioPropiedad

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/propiedad', methods=('POST'))
def agregar_propiedad():
    try:
        propiedad_dict = request.json

        map_reserva = MapeadorPropiedadDTOJson()
        reserva_dto = map_reserva.externo_a_dto(propiedad_dict)

        sr = ServicioPropiedad()
        dto_final = sr.crear_reserva(reserva_dto)

        return map_reserva.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/reserva', methods=('GET',))
@bp.route('/reserva/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioPropiedad()
        
        return sr.obtener_propiedad_por_id(id)
    else:
        return [{'message': 'GET!'}]