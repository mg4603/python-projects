from flask import Flask, render_template
from os import makedirs, urandom
from os.path import join

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=urandom(24).hex(),
        DATABASE=join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    from .db import init_app
    init_app(app)

    @app.route("/")
    def index():
        return "Hello World"

    return app