import json

import requests

from openweather_api import OpenWeather


class ForecastAPI(OpenWeather):
    def __init__(self):
        super().__init__()
        self.url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric'

    def connection(self):
        url = self.url.format(lat=50, lon=50, API_key=self.API_KEY)
        response = requests.get(url)
        return response.status_code

    def get(self, lat: float, lon: float) -> dict | None:
        url = self.url.format(lat=lat, lon=lon, API_key=self.API_KEY)
        try:
            response = requests.get(url)
            return response.json()
        except requests.exceptions.RequestException as expt:
            print(expt)
            return None


if __name__ == "__main__":
    weather_api = ForecastAPI()
    print(json.dumps(weather_api.get(lat=50.0833, lon=19.9167), indent=2))
