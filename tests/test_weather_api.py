import unittest

from weather_api import WeatherAPI


class TestWeatherAPI(unittest.TestCase):

    def test_connection(self):
        weather_api = WeatherAPI()
        self.assertTrue(weather_api.connection(), 400)

    def test_get_city_name(self):
        weather = WeatherAPI()
        self.assertIsNotNone(weather.get('London'))


if __name__ == '__main__':
    unittest.main()
