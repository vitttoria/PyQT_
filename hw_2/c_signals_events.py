"""
Реализация программы проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui

from ui.c_signals_events_py import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.ui.pushButtonRT.clicked.connect(self.MoveToRT)
        self.ui.pushButtonLB.clicked.connect(self.MoveToLB)
        self.ui.pushButtonRB.clicked.connect(self.MoveToRB)
        self.ui.pushButtonCenter.clicked.connect(self.MoveToCenter)
        self.ui.pushButtonMoveCoords.clicked.connect(self.on_changedX)
        # self.ui.pushButtonMoveCoords.clicked.connect(self.on_changedY)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetData)

    def MoveToRT(self):
        """
        Обработка сигнала clicked для кнопки pushButtonRT

        :return: None
        """

        current_pos = QtWidgets.QApplication.screenAt(self.pos())
        screen_size_width = current_pos.size().width()
        print(current_pos.size().width())
        print(self.width())

        position_x = screen_size_width - self.width()
        print(position_x)

        self.move(position_x, 0)

    def MoveToLB(self):
        """
        Обработка сигнала clicked для кнопки pushButtonLB

        :return: None
        """

        current_pos = QtWidgets.QApplication.screenAt(self.pos())
        screen_size_height = current_pos.size().height()

        position_y = screen_size_height - self.height()

        self.move(0, position_y)

    def MoveToRB(self):
        """
        Обработка сигнала clicked для кнопки pushButtonRB

        :return: None
        """

        current_pos = QtWidgets.QApplication.screenAt(self.pos())
        screen_size_width = current_pos.size().width()
        screen_size_height = current_pos.size().height()
        position_x = screen_size_width - self.width()
        position_y = screen_size_height - self.height()

        self.move(position_x, position_y)

    def MoveToCenter(self):
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCenter

        :return: None
        """

        current_pos = QtWidgets.QApplication.screenAt(self.pos())
        screen_size_width = current_pos.size().width()
        screen_size_height = current_pos.size().height()

        position_x = (screen_size_width - self.width()) / 2
        position_y = (screen_size_height - self.height()) / 2
        print(position_x, position_y)

        self.move(position_x, position_y)

    def on_changedX(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCoords

        :return: None
        """

        self.move(self.ui.pushButtonMoveCoords.y(), self.ui.pushButtonMoveCoords.x())

    # def on_changedY(self) -> None:
    #     self.move(self.ui.pushButtonMoveCoords.x(), self.ui.spinBoxY.value())

    def onPushButtonGetData(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonGetData

        :return: None
        """
        center = self.rect().center()
        self.ui.plainTextEdit.setPlainText(
            str(QtWidgets.QApplication.screens()) + "\n" +
            str(QtWidgets.QApplication.primaryScreen()) + "\n" +
            str(self.screen().geometry()) + "\n" +
            str(self.screen()) + "\n" +
            str(self.size()) + "\n" +
            str(self.minimumSize()) + "\n" +
            str(self.pos()) + "\n" +
            str(self.mapToGlobal(center)) + "\n" +
            str(QtWidgets.QMainWindow.windowState) + "\n" +
            str(time.ctime()))

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения положения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """

        print(event.oldPos())
        print(event.pos())
        print()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """

        print(event.size())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
