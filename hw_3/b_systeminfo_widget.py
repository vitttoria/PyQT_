"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from hw_3.a_threads import SystemInfo
from ui.load_cpu_ram_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initThreads(self) -> None:
        """Инициализация потоков"""
        self.SystemInfothread = SystemInfo()
        self.SystemInfothread.start()

    def initSignals(self) -> None:
        """Инициализация сигналов"""

        self.ui.time_lineEdit.textChanged.connect(self.delay)
        self.SystemInfothread.systemInfoReceived.connect(self.updInfo)

    def updInfo(self, system_info):
        load_cpu, load_ram = system_info
        self.ui.CPU_plainTextEdit.setPlainText(f"{load_cpu}%")
        self.ui.RAM_plainTextEdit.setPlainText(f"{load_ram}%")

    def delay(self, delay):
        try:
            delay = float(delay)
            self.SystemInfothread.delay = delay
        except ValueError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Window()
    widget.show()
    sys.exit(app.exec())