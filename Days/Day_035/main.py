import requests

MY_LAT = 000000000
MY_LONG = 00000000
API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

try:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False
    if "list" in weather_data:
        for hour_data in weather_data["list"]:
            condition_code = hour_data["weather"][0]["id"]
            if int(condition_code) < 700:
                will_rain = True
                break

    if will_rain:
        print("Bring an umbrella.")
    else:
        print("No need for an umbrella.")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)
except KeyError as e:
    print("KeyError:", e)
