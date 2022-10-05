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

if __name__ == "__main__":
    app.run(debug=True)