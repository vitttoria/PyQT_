"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""

import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from hw_3.a_threads import WeatherHandler
from ui.weather_api_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initThreads(self) -> None:
        """Инициализация потоков"""
        self.WeatherThread = WeatherHandler(0, 0)

    def initSignals(self) -> None:
        """Инициализация сигналов"""
        self.ui.lineEdit.textChanged.connect(self.delay)
        self.ui.start_pushButton.clicked.connect(self.lat_lon_input)
        self.ui.start_pushButton.clicked.connect(self.stopThread)

    def lat_lon_input(self):
        if self.WeatherThread is None or not self.WeatherThread.isRunning():
            lat = self.ui.shirota_lineEdit.text()
            lon = self.ui.dolgota_lineEdit.text()
            # delay = float(self.delay.text())

            self.WeatherThread = WeatherHandler(lat, lon)
            # self.WeatherThread.setDelay(delay)
            self.WeatherThread.weatherData.connect(self.updInfo)
            self.WeatherThread.start()

            self.ui.shirota_lineEdit.setEnabled(False)
            self.ui.dolgota_lineEdit.setEnabled(False)
            self.ui.lineEdit.setEnabled(False)
            self.ui.start_pushButton.setText("Стоп")
        else:
            self.WeatherThread.quit()
            self.WeatherThread.wait()
            self.WeatherThread = None

    def updInfo(self, weather_info):
        lat, lon = weather_info
        self.ui.shirota_lineEdit.setText(lat)
        self.ui.dolgota_lineEdit.setText(lon)

    def stopThread(self):
        if self.WeatherThread.isFinished():
            self.WeatherThread.weatherData.connect(self.updInfo)
            self.WeatherThread.finished()
            self.ui.shirota_lineEdit.setEnabled(True)
            self.ui.dolgota_lineEdit.setEnabled(True)
            self.ui.lineEdit.setEnabled(True)
            self.ui.start_pushButton.setText("Старт")

    def delay(self):
        self.WeatherThread.setDelay(self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Window()
    widget.show()
    sys.exit(app.exec())
