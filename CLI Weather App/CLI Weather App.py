import argparse
import requests


# -------------------------------
# Context Manager for Weather API
# -------------------------------
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def __enter__(self):
        self.session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

    def get_weather(self, city, units="metric"):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": units
        }

        response = self.session.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()


# -------------------------------
# Utility Function
# -------------------------------
def format_weather(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }


# -------------------------------
# CLI Logic
# -------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Command Line Weather Application"
    )

    parser.add_argument(
        "city",
        help="City name (e.g. Nairobi)"
    )

    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="Temperature units (metric = °C, imperial = °F)"
    )

    parser.add_argument(
        "--api-key",
        required=True,
        help="OpenWeatherMap API key"
    )

    args = parser.parse_args()

    try:
        with WeatherAPI(args.api_key) as api:
            raw_data = api.get_weather(args.city, args.units)
            weather = format_weather(raw_data)

            unit_symbol = "°C" if args.units == "metric" else "°F"

            print("\nWeather Information")
            print("-" * 30)
            print(f"City: {weather['city']}")
            print(f"Temperature: {weather['temperature']}{unit_symbol}")
            print(f"Condition: {weather['description'].title()}")
            print(f"Humidity: {weather['humidity']}%")

    except requests.exceptions.HTTPError:
        print("❌ Error: City not found or invalid API key.")
    except requests.exceptions.RequestException:
        print("❌ Network error. Check your internet connection.")
    except KeyError:
        print("❌ Unexpected API response format.")
    except Exception as e:
        print("❌ Error:", e)


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    main()
