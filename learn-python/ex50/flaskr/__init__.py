from os import makedirs
from os.path import join
from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config == None:
        # load instance config, if it exits when, not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load test_config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "Hello, World!"
        
    return app