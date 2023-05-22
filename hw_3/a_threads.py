"""
Модуль в котором содержаться потоки Qt
"""

import time

import psutil
import requests as requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent()
            self.systemInfoReceived.emit([cpu_value, ram_value])
            time.sleep(self.delay)


class WeatherHandler(QtCore.QThread):
    weatherData = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:

        while self.__status:
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherData.emit(data)
            time.sleep(self.__delay)
