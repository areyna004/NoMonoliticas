import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import pda.modulos.propiedades.aplicacion
    import pda.modulos.propietarios.aplicacion

def importar_modelos_alchemy():
    import pda.modulos.propiedades.infraestructura.dto
    import pda.modulos.propietarios.infraestructura.dto


def comenzar_consumidor():
    import threading
    import pda.modulos.propietarios.infraestructura.consumidores as propietarios
    import pda.modulos.propiedades.infraestructura.consumidores as propiedades

    # Suscripción a eventos
    threading.Thread(target=propiedades.suscribirse_a_eventos).start()
    threading.Thread(target=propietarios.suscribirse_a_eventos).start()
    

    # Suscripción a comandos
    threading.Thread(target=propiedades.suscribirse_a_comandos).start()
    threading.Thread(target=propietarios.suscribirse_a_comandos).start()


def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

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