"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QMainWindow, QWidget

from b_systeminfo_widget import Ui_MainWindow
from c_weatherapi_widget import Ui_WeatherAPI


class ComboWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboWidget")

        b_systeminfo_widget = Ui_MainWindow()
        c_weatherapi_widget = Ui_WeatherAPI()

        layout = QVBoxLayout()
        layout.addWidget(b_systeminfo_widget)
        layout.addWidget(c_weatherapi_widget)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        comboWidget = ComboWidget()
        self.setCentralWidget(comboWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
