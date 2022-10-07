from flask import Flask, render_template
from os import makedirs, urandom
from os.path import join

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=urandom(24).hex(),
        DATBASE=join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        return "Hello world"
    return app