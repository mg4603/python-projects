from configparser import ConfigParser
from flask import Flask

def openweather_api():
    config = ConfigParser()
    config.read("../../config/keys_config.cfg")
    return config.get("openweather", "api_key")

API_KEY = openweather_api()

app = Flask(__name__)

@app.route("/")
def hello():
    return f"""
    <h1>Hello Gators!<h1>
    <p><a href="/user/Lol">Click me!</a></p>
    """

@app.route("/user/<name>")
def user(name):
    return f"""
    <h1>Hello {name}!</h1>
    <p>Change the name in the browser <em>address bar</em> and reload
    the page.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)