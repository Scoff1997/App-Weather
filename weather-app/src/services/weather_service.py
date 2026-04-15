from src.api.weather_api import fetch_weather

CITIES = {
    "roma": (41.9028, 12.4964),
    "milano": (45.4642, 9.1900),
    "napoli": (40.8518, 14.2681),
    "torino": (45.0703, 7.6869),
}

def get_weather_by_city(city_name):
    city_name = city_name.lower()

    if city_name not in CITIES:
        raise ValueError("Città non trovata nel database.")

    lat, lon = CITIES[city_name]
    data = fetch_weather(lat, lon)

    current = data["current_weather"]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "weathercode": current["weathercode"]
    }

# ⬇️ AGGIUNGI QUI LA FUNZIONE DELLA PREVISIONE A 5 GIORNI

import requests
from datetime import datetime

def get_five_day_forecast(lat, lon):
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            "&daily=temperature_2m_max,temperature_2m_min,weathercode"
            "&timezone=auto"
        )

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        daily = data.get("daily")

        if not daily:
            raise ValueError("La risposta dell'API non contiene dati giornalieri.")

        dates = daily["time"]
        tmax = daily["temperature_2m_max"]
        tmin = daily["temperature_2m_min"]
        codes = daily["weathercode"]

        print("\n📅 Previsione meteo a 5 giorni:\n")

        for i in range(5):
            day = datetime.strptime(dates[i], "%Y-%m-%d").strftime("%d %b %Y")
            print(f"➡️  {day}")
            print(f"   🌡️ Max: {tmax[i]}°C | Min: {tmin[i]}°C")
            print(f"   ☁️ Weather code: {codes[i]}")
            print()

    except Exception as e:
        print("Errore durante il recupero della previsione:", e)
