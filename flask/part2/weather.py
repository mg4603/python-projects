from configparser import ConfigParser
from flask import Flask
from requests import get

API_URL = ('https://api.openweathermap.org/data/2.5/weather?zip={},{}&mode=json&units=imperial&appid={}')


def openweather_api(path):
    """Get API key of openweather api using configparser and local
    .cfg file"""
    config = ConfigParser()
    config.read(path)
    return config.get("openweather", "api_key")

def query_openweather_api(zip, country_code):
    try:
        data = get(API_URL.format(zip, country_code, API_KEY)).json()
    except Exception as e:
        print(e)
        data = None
    return data

API_KEY = openweather_api("../../config/keys_config.cfg")

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