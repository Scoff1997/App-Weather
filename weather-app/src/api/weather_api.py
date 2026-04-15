import requests
from src.config.config import BASE_URL

def fetch_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()