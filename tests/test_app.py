import logging
import numbers
import os
import unittest
import _tkinter
from parameterized import parameterized

from src.weather_app import *

logging.basicConfig(format='%(levelname)s:%(module)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        os.chdir('../src')
        self.app = App()
        logger.info('Weather app started')

    def tearDown(self):
        self.app.quit()
        self.app.destroy()
        logger.info('Weather app destroyed')

    @parameterized.expand(["London", "Paris", "Kraków", "Warsaw", "New York"])
    def test_app(self, city):
        title = self.app.winfo_toplevel().title()
        self.assertEqual(title, 'Aurëa')
        logger.info('Weather app title correct')

        self.app.city_entry.insert(0, city)
        self.app.search_btn_callback()
        self.assertEqual(self.app.location_lbl._text, city)
        logger.info('Entry checked')

        self.assertIsInstance(float(self.app.temperature_lbl._text[0:-2]), numbers.Number)
        logger.info('Basic response checked')


if __name__ == '__main__':
    unittest.main()
