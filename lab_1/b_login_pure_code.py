from PySide6 import QtWidgets


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        """
        Доинициализация Ui

        :return: None
        """
        # self.setFixedSize(250, 150)
        self.setWindowTitle("Вход в приложение")
        self.setFixedSize(350, 200)

        labelLogin = QtWidgets.QLabel()
        labelLogin.setText("Логин")
        labelLogin.setMinimumWidth(45)

        labelPassword = QtWidgets.QLabel()
        labelPassword.setText("Пароль")
        labelPassword.setMinimumWidth(45)

        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditLogin.setPlaceholderText("Введите логин")
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setPlaceholderText("Введите пароль")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.pushButtonRegistration = QtWidgets.QPushButton()
        self.pushButtonRegistration.setText('Регистрация')
        self.pushButtonOk = QtWidgets.QPushButton()
        self.pushButtonOk.setText('Ок')
        self.pushButtonCancel = QtWidgets.QPushButton()
        self.pushButtonCancel.setText('Отмена')

        # layouts

        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(labelPassword)
        layoutPassword.addWidget(self.lineEditPassword)

        layoutRegistration = QtWidgets.QHBoxLayout()
        layoutRegistration.addSpacerItem(
                QtWidgets.QSpacerItem(
                    20, 10, QtWidgets.QSizePolicy.Policy.Expanding
                )
        )
        layoutRegistration.addWidget(self.pushButtonRegistration)

        layoutHandle = QtWidgets.QHBoxLayout()
        layoutHandle.addSpacerItem(
                QtWidgets.QSpacerItem(
                    20, 10, QtWidgets.QSizePolicy.Policy.Expanding
                )
        )

        layoutHandle.addWidget(self.pushButtonOk)
        layoutHandle.addWidget(self.pushButtonCancel)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addSpacerItem(
            QtWidgets.QSpacerItem(
                10, 20, vData=QtWidgets.QSizePolicy.Policy.Expanding
            )
        )
        layoutMain.addLayout(layoutRegistration)
        layoutMain.addLayout(layoutHandle)

        self.setLayout(layoutMain)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    win_1 = MyFirstWindow()
    win_1.show()

    app.exec()
