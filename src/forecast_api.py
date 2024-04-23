import json
from datetime import datetime

import requests

from openweather_api import OpenWeather


class ForecastAPI(OpenWeather):
    def __init__(self):
        super().__init__()
        self.url = ('https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={'
                    'API_key}&units=metric')

    def connection(self):
        url = self.url.format(lat=50, lon=50, cnt=40, API_key=self.API_KEY)
        response = requests.get(url)
        return response.status_code

    def get(self, lat: float, lon: float, cnt=24) -> dict | None:
        url = self.url.format(lat=lat, lon=lon, cnt=cnt, API_key=self.API_KEY)
        try:
            response = requests.get(url)
            return response.json()
        except requests.exceptions.RequestException as expt:
            print(expt)
            return None

    def get_forecast(self, lat: float, lon: float, cnt=24) -> list[dict] | None:
        data = self.get(lat=lat, lon=lon, cnt=cnt)

        if data['cod'] == '200':
            raw_list = data['list']
            forecast_list = []
            for item in raw_list:
                record = {'datetime': datetime.fromtimestamp(int(item['dt'])).strftime('%H:%M %A'),
                          'icon': item['weather'][0]['icon'],
                          'description': item['weather'][0]['description'],
                          'temp': str(item['main']['temp']) + ' ℃'}

                forecast_list.append(record)

            return forecast_list
        else:
            return None


if __name__ == "__main__":
    weather_api = ForecastAPI()
    print(json.dumps(weather_api.get(lat=50.0833, lon=19.9167), indent=2))
    print(weather_api.get_forecast(lat=50.0833, lon=19.9167))
