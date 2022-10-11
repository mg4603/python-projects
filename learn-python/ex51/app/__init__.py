from flask import Flask
from os.path import join
from os import makedirs
from .views.hello import bp as hello_bp

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
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
    
    app.register_blueprint(hello_bp)
    
    @app.route('/hello/q?greet=<greet>&name=<name>')
    def hello(greet , name):
        return "%s, %s" %(greet, name)

    return app