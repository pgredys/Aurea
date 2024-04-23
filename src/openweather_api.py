from abc import ABC, abstractmethod
from pathlib import Path

from dotenv import dotenv_values


class OpenWeather(ABC):
    def __init__(self):
        self.API_KEY = dotenv_values(Path.joinpath(Path(__file__).parent, ".env")).get("API_KEY")

    @abstractmethod
    def connection(self):
        pass

    @abstractmethod
    def get(self, *args):
        pass
