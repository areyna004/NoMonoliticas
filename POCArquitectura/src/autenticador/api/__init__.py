import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import autenticador.modulos.usuarios.infraestructura.dto

def create_app(configuracion=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:U6yEZgrAjc6c1olP@34.66.105.29:3306/db-autenticador'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from autenticador.config.db import init_db
    init_db(app)

    from autenticador.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

    from . import autenticador

    app.register_blueprint(autenticador.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    with app.app_context():
        db.create_all()

    return app
