"""
Реализация программы взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QDial
import sys

from ui.d_eventfilter_settings_ui import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("oct")
        self.ui.comboBox.addItem("hex")
        self.ui.comboBox.addItems(["bin", "dec"])
        self.ui.comboBox.insertItem(0, "")

        # self.loadData()
        self.initSignals()
        self.ui.dial.installEventFilter(self)

    # def loadData(self) -> None:
    #     """
    #     Загрузка данных в Ui
    #
    #     :return: None
    #     """
    #
    #     self.ui.comboBox.setCurrentText(self.settings.value("Формат", ""))
    #     self.ui.lcdNumber.display(self.settings.value("Значение", ""))

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.ui.dial.valueChanged.connect(self.dial_changed)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_moved)
        self.ui.lcdNumber.display(self.change_form(self.ui.dial.value()))
        self.ui.comboBox.currentTextChanged.connect(self.combobox_change)

    def PressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Установка значений кнопками клавиатуры (+, -)
        :param self:
        :param event:
        :return: 
        """
        if event.key() == QtCore.Qt.Key.Key_Plus:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        if event.key() == QtCore.Qt.Key.Key_Minus:
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def change_form(self, value):
        """
        Установка формата отображаемого значения в зависимости от выбранного в comboBox параметра value
        :return:
        """
        if self.ui.comboBox.currentText() == "oct":
            return oct(value)
        if self.ui.comboBox.currentText() == "hex":
            return hex(value)
        if self.ui.comboBox.currentText() == "bin":
            return bin(value)
        if self.ui.comboBox.currentText() == "dec":
            return value

    def dial_changed(self):
        """
        Обработка сигнала valuechanched для dial
        :return: None
        """
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
        self.ui.lcdNumber.display(self.ui.dial.value())

    def slider_moved(self):
        """
        Обработка сигнала valuechanged для horizontalslider
        :return:
        """
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())

    def combobox_change(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна и сохранения данных

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.settings.setValue(self.ui.comboBox.currentText())
        self.settings.setValue(self.ui.lcdNumber.value())

    def closeWindowEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        answer = QtWidgets.QMessageBox.question(self, "Закрыть окно?", "Вы действительно хотите закрыть окно?")

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
