import logging
import unittest

from parameterized import parameterized

from src.weather_api import WeatherAPI

logging.basicConfig(format='%(levelname)s:%(module)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        self.weather_api = WeatherAPI()

    def test_connection(self):
        logger.info('Testing connection to weather api')
        answer = self.weather_api.connection()
        self.assertEqual(200, answer)
        logger.info(f'Connection to weather api code: {answer}\n')

    @parameterized.expand(["London", "Paris", "Krakow", "Warsaw", "New York"])
    def test_get_city_name(self, city):
        logger.info('Testing get_city_name method')
        answer = self.weather_api.get('London')
        self.assertIsNotNone(answer)
        self.assertIsNotNone(answer['weather'])
        logger.info(f'Weather in {city}: {answer["weather"][0]}\n')


if __name__ == '__main__':
    unittest.main()
