import json
from pathlib import Path
import requests
from dotenv import dotenv_values


class WeatherAPI:
    def __init__(self):
        self.API_KEY = dotenv_values(Path.joinpath(Path(__file__).parent, ".env")).get("API_KEY")
        self.url_city_name = ("https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={"
                              "API_key}&units=metric")

    def connection(self):
        url = self.url_city_name.format(city_name='London, uk', API_key=self.API_KEY)
        response = requests.get(url)
        return response.status_code

    def get(self, city_name: str) -> dict | None:
        url = self.url_city_name.format(city_name=city_name, API_key=self.API_KEY)
        try:
            response = requests.get(url)
            return response.json()
        except requests.exceptions.RequestException:
            print(requests.exceptions.RequestException)
            return None


if __name__ == "__main__":
    weather_api = WeatherAPI()
    print(json.dumps(weather_api.get(city_name='London, uk'), indent=2))
