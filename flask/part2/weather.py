from configparser import ConfigParser

def openweather_api():
    config = ConfigParser()
    config.read("../config/keys_config.cfg")
    return config.get("openweather", "api_key")

API_KEY = openweather_api()