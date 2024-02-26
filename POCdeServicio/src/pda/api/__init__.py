import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la DB
    from pda.config.db import init_db
    init_db(app)
    from pda.config.db import db
    with app.app_context():
        db.create_all()

    # Importa Blueprints
    from . import arrendatarios
    from . import propiedades
    from . import propietarios
    from . import transacciones
    from . import usuario

    # Registro de Blueprints
    app.register_blueprint(arrendatarios.bp)
    app.register_blueprint(propiedades.bp)
    app.register_blueprint(propietarios.bp)
    app.register_blueprint(transacciones.bp)
    app.register_blueprint(usuario.bp)

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