import logging
import numbers
import unittest

from parameterized import parameterized

from src.weather import Weather
from src.weather_api import WeatherAPI

logging.basicConfig(format='%(levelname)s:%(module)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        logger.info('Setting up...')
        self.weather_api = WeatherAPI()

    @parameterized.expand(["London", "Paris", "Kraków", "Warsaw", "New York"])
    def test_weather(self, city):
        weather_response = self.weather_api.get(city)
        weather = Weather(weather_response)

        logger.info(f'Weather in {city}: {weather}\n')
        self.assertIsNotNone(weather)
        self.assertIsInstance(weather.weather, dict)
        self.assertTrue(weather.temp, numbers.Number)
        self.assertIsInstance(weather.feels_like, numbers.Number)
        self.assertIsInstance(weather.pressure, numbers.Number)
        self.assertIsInstance(weather.humidity, numbers.Number)
        self.assertIsInstance(weather.wind, dict)
        self.assertIsInstance(weather.clouds, dict)
        self.assertIsInstance(weather.sunrise, str)
        self.assertIsInstance(weather.sunset, str)


if __name__ == '__main__':
    unittest.main()
