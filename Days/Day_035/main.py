import requests
 
MY_LAT = 00000000
MY_LONG = 00000000
API_KEY = "xxxxxxxxxxxxxxxxxxxxx"
 
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}
 
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
print(data)