import os
from flask import Flask, render_template
from .modules import make_ordinal, convert_to_dict, presidency_president_pairs_list

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # load instance config if it exists when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    pres_list = convert_to_dict("flaskr/presidents.csv")

    @app.route("/")
    def index():
        return render_template("index.html", 
                            pairs=presidency_president_pairs_list(pres_list),
                            the_title="Presidents Index")
    
    @app.route("/user/<name>")
    def user(name):
        return render_template("hello.html", name=name)
    
    @app.route("/president/<num>")
    def detail(num):
        try:
            pres_dict = pres_list[int(num)-1]
        except:
            return f"<h1>Invalid value for presidency: {num}</h1>"
        ord_num = make_ordinal(int(num))
        return render_template("president.html", pres=pres_dict, 
                                ord=ord_num, the_title=pres_dict["President"])

    return app