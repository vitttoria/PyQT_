from PySide6 import QtWidgets


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initDB()
        self.initSignals()

    def initUI(self):
        """
        Доинициализация Ui

        :return: None
        """
        # self.setFixedSize(250, 150)
        self.setWindowTitle("Вход в приложение")
        self.setFixedSize(350, 200)

    def initSignals(self) -> None:
        """
    Инициализация сигналов

    :return: None
    """

    pass

    def initChilds(self) -> None:
        pass

    def initDB(self) -> None:
        pass

    def initThreads(self) -> None:
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    win_1 = MyFirstWindow()
    win_1.show()

    app.exec()
