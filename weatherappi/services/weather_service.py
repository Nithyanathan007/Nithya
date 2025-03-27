import requests
from models.weather_model import Weather

API_KEY = "ceb66ffa5742919ddaac9b9dbc26908b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_report(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = Weather(
            city=data["name"],
            temperature=data["main"]["temp"],
            description=data["weather"][0]["description"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"]
        )
        return weather.to_dict()
    else:
        return {"error": "City not found"}
