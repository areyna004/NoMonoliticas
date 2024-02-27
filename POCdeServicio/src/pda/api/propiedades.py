import pda.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response

from pda.seedwork.dominio.excepciones import ExcepcionDominio
from pda.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from pda.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from pda.modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from pda.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from pda.seedwork.aplicacion.queries import ejecutar_query
from pda.seedwork.aplicacion.comandos import ejecutar_commando
from pda.modulos.propiedades.infraestructura.despachadores import Despachador

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/propiedad', methods=['POST'])
def agregar_propiedad():
    '''
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        sr = ServicioPropiedad()
        dto_final = sr.crear_propiedad(propiedad_dto)
        return map_propiedad.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    '''
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(propiedad_dto.fecha_creacion, propiedad_dto.fecha_actualizacion, propiedad_dto.id, propiedad_dto.nombre, propiedad_dto.descripcion, propiedad_dto.tamanio, propiedad_dto.tipo, propiedad_dto.direcciones)
        despachador = Despachador()

        despachador.publicar_comando(comando, 'comandos-propiedad')
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedad', methods=['GET'])
@bp.route('/propiedad/<id>', methods=['GET'])
def dar_propiedad(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_propiedad = MapeadorPropiedadDTOJson()
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    
    else:
        sr = ServicioPropiedad()
        return sr.obtener_todas_las_propiedades()
    