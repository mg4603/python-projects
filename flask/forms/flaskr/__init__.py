from flask import Flask, render_template, request, url_for, flask, redirect
from os.path import join
from os import makedirs, urandom

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=urandom(24).hex(),
        DATABASE=join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try:
        makedirs(app.instance_path)
    except OSError:
        pass
    
    messages = [
        {
            "title": "Message One",
            "content": "Message One Content"
        },
        {
            "title": "Message Two",
            "content": "Message Two Content"
        }
    ]

    @app.route("/")
    def index():
        return render_template("index.html", messages=messages)

    @app.route("/create/", methods=('GET', 'POST'))
    def create():
        return render_template("create.html")

    return app