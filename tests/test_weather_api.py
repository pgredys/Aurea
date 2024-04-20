import unittest

import logging

from weather_api import WeatherAPI

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        self.weather_api = WeatherAPI()
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__file__)

    def test_connection(self):
        logger.info(f'Testing connection to weather api')
        answer = self.weather_api.connection()
        self.assertEqual(200, answer)
        logger.info(f'Connection to weather api code: {answer}\n')

    def test_get_city_name(self):
        logger.info(f'Testing get_city_name method')
        city = 'London'
        answer = self.weather_api.get('London')
        self.assertIsNotNone(answer)
        self.assertIsNotNone(answer['weather'])
        logger.info(f'Weather in {city}: {answer["weather"][0]}')


if __name__ == '__main__':
    unittest.main()
