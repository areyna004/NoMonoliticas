import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

from . import servicios_externos

def create_app(configuracion={}):
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')
    
    app.register_blueprint(servicios_externos.bp)

    @app.route("/spec", methods=["GET"])
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Propiedades de los Andes"
        return jsonify(swag)

    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "up"}

    return app