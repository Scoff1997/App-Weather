def show_weather(city, weather):
    print("\n🌤 WEATHER APP")
    print("-------------------")
    print(f"📍 Città: {city}")
    print(f"🌡 Temperatura: {weather['temperature']}°C")
    print(f"💨 Vento: {weather['windspeed']} km/h")
    print(f"🌈 Codice meteo: {weather['weathercode']}")