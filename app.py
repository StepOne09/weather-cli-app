import requests

API_KEY = "9ce7d647f8511b81064fca40c9ab39fe"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print(data)  # debug

    cod = str(data.get("cod"))

    if cod != "200":
        print("\nError:", data.get("message"))
        return

    print("\n===== WEATHER REPORT =====\n")
    print("City:", data["name"])
    print("Temp:", data["main"]["temp"])
    print("Humidity:", data["main"]["humidity"])
    print("Condition:", data["weather"][0]["description"])

city = input("Enter city name: ")
get_weather(city)

