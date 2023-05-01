from PySide6 import QtWidgets

from hw_1.ui.login_ui import Ui_LoginForm


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        # self.ui.pushButton.setHidden(True)  # скрыть кнопку
        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    win_1 = MyFirstWindow()
    win_1.show()

    app.exec()