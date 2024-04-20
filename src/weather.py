from dataclasses import dataclass


@dataclass
class Weather:
    """data class to hold weather data"""
    weather: dict
    temp: float
    feels_like: float
    pressure: float
    humidity: float
    wind: dict
    clouds: dict
    sunrise: int
    sunset: int

    def __init__(self, response: dict):
        self.weather = response['weather'][0]
        self.temp = response['main']['temp']
        self.feels_like = response['main']['feels_like']
        self.pressure = response['main']['pressure']
        self.humidity = response['main']['humidity']
        self.wind = response['wind']
        self.clouds = response['clouds']
        self.sunrise = response['sys']['sunrise']
        self.sunset = response['sys']['sunset']
