# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherapi_MWZIdVZZ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(408, 416)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 382, 339))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.coordinates_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.coordinates_groupBox.setObjectName(u"coordinates_groupBox")
        self.gridLayout_2 = QGridLayout(self.coordinates_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shirota_label = QLabel(self.coordinates_groupBox)
        self.shirota_label.setObjectName(u"shirota_label")
        self.shirota_label.setMinimumSize(QSize(100, 0))
        self.shirota_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.shirota_label)

        self.shirota_lineEdit = QLineEdit(self.coordinates_groupBox)
        self.shirota_lineEdit.setObjectName(u"shirota_lineEdit")

        self.horizontalLayout.addWidget(self.shirota_lineEdit)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.shirota_label_3 = QLabel(self.coordinates_groupBox)
        self.shirota_label_3.setObjectName(u"shirota_label_3")
        self.shirota_label_3.setMinimumSize(QSize(100, 0))
        self.shirota_label_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.shirota_label_3)

        self.dolgota_lineEdit = QLineEdit(self.coordinates_groupBox)
        self.dolgota_lineEdit.setObjectName(u"dolgota_lineEdit")

        self.horizontalLayout_3.addWidget(self.dolgota_lineEdit)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.coordinates_groupBox, 0, 0, 1, 1)

        self.weather_groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.weather_groupBox.setObjectName(u"weather_groupBox")
        self.gridLayout_3 = QGridLayout(self.weather_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.weather_label = QLabel(self.weather_groupBox)
        self.weather_label.setObjectName(u"weather_label")
        self.weather_label.setMinimumSize(QSize(100, 0))
        self.weather_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.weather_label)

        self.weather_plainTextEdit = QPlainTextEdit(self.weather_groupBox)
        self.weather_plainTextEdit.setObjectName(u"weather_plainTextEdit")
        self.weather_plainTextEdit.setMaximumSize(QSize(16777215, 30))
        self.weather_plainTextEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.weather_plainTextEdit)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.weather_groupBox, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.time_label = QLabel(self.scrollAreaWidgetContents)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(150, 0))
        self.time_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.time_label)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.start_pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.start_pushButton.setObjectName(u"start_pushButton")

        self.gridLayout_4.addWidget(self.start_pushButton, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 408, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.coordinates_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.shirota_label.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.shirota_label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.weather_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.weather_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438, \u0441", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442/\u0421\u0442\u043e\u043f", None))
    # retranslateUi

