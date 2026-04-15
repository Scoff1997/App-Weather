from src.services.weather_service import get_weather_by_city, get_five_day_forecast, CITIES
from src.ui.display import show_weather

def main():
    print("🌍 Weather App")
    city = input("Inserisci città (roma, milano, napoli, torino): ").lower()

    print("\nScegli un'opzione:")
    print("1) Meteo attuale")
    print("2) Previsione a 5 giorni")

    choice = input("Seleziona 1 o 2: ")

    try:
        if city not in CITIES:
            raise ValueError("Città non trovata nel database.")

        if choice == "1":
            weather = get_weather_by_city(city)
            show_weather(city, weather)

        elif choice == "2":
            lat, lon = CITIES[city]
            get_five_day_forecast(lat, lon)

        else:
            print("❌ Scelta non valida.")

    except ValueError as e:
        print("❌ Errore:", e)
    except Exception as e:
        print("⚠️ Errore generico:", e)

if __name__ == "__main__":
    main()
