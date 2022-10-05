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

def query_openweather_api(zip, country_code, api_key):
    """Add fn to query openweather api with zip, country code and api_key
    """
    try:
        data = get(API_URL.format(zip, country_code, api_key)).json()
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

@app.route('/weather/<zip>/<country_code>')
def result(zip, country_code):
    resp = query_openweather_api(zip, country_code, API_KEY)
    try:
        text = f"""{resp["name"]} temperature is {resp["main"]["temp"]}
        degrees Fahrenheit with {resp["weather"][0]["description"]}.        
        """
    except:
        text = f"""There was an error.<br>Did you include a valid 
        {country_code.upper()} zip code in the URL"""
    
    return text

if __name__ == "__main__":
    app.run(debug=True)