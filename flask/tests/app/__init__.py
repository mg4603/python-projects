from flask import Flask
from os import makedirs, urandom
from os.path import join
from .db import register_db
from .auth import bp as auth_bp

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=urandom(24).hex(),
        DATABASE=join(app.instance_path, 'app.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass
    
    register_db(app)
    app.register_blueprint(auth_bp)

    return app