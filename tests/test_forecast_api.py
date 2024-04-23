import logging
import unittest

from parameterized import parameterized

from src.forecast_api import ForecastAPI

logging.basicConfig(format='%(levelname)s:%(module)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.forecast_api = ForecastAPI()

    def test_connection(self):
        logger.info('Testing connection to weather api')
        answer = self.forecast_api.connection()
        self.assertEqual(200, answer)
        logger.info(f'Connection to weather api code: {answer}\n')

    @parameterized.expand([[-40.8, -65.2, 4], [-43.5, 172.6, 8], [35.14, 136.9, 40], [44.8, -0.6, 10], [-1, 32.5, 24]])
    def test_get(self, lat=50, lon=50, cnt=5):
        logger.info('Testing forecast api get method')
        answer = self.forecast_api.get(lat, lon, cnt)
        self.assertIsNotNone(answer)
        self.assertEqual('200', answer['cod'])
        logger.info(f'Got forecast in {answer['city']['name']} for {3 * len(answer['list'])} hours\n')

    @parameterized.expand([[-40.8, -65.2, 4], [-43.5, 172.6, 8], [35.14, 136.9, 40], [44.8, -0.6, 10], [-1, 32.5, 24]])
    def test_get_forecast(self, lat, lon, cnt):
        logger.info('Testing forecast api get_forecast method')
        answer = self.forecast_api.get_forecast(lat, lon, cnt)
        self.assertIsNotNone(answer)
        self.assertIsInstance(answer, list)
        self.assertTrue(cnt, len(answer))
        for item in answer:
            self.assertIsInstance(item, dict)
            self.assertTrue('datetime' in item)
            self.assertTrue('icon' in item)
            self.assertTrue('description' in item)
            self.assertTrue('temp' in item)
        logger.info('Forecast contains required data')
        logger.info(f'Got forecast in for {len(answer)} 3-hours time window\n')


if __name__ == '__main__':
    unittest.main()
