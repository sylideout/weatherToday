import json
import requests

with open('./api_keys.json') as api_keys_file:
    api_keys = json.load(api_keys_file)

WEATHER_API = api_keys.get('weatherAPI')

REQUEST_URL = f"https://api.weatherapi.com/v1/"

def get_forecast(
    q: str,         # location
    days: int,      # number of days of weather forecast
):
    URL = (
        f'{REQUEST_URL}forecast.json?' \
        f'q={q}&' \
        f'days={days}&' \
        f'key={WEATHER_API}'
    )
    print(URL)

    response = requests.get(URL, timeout=5)
    data = response.json()

    return data

data = get_forecast("london", 1)
print(data)
