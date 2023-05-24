# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadxKPQYt.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(451, 246)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_label = QLabel(self.centralwidget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(150, 0))
        self.time_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.time_label)

        self.time_lineEdit = QLineEdit(self.centralwidget)
        self.time_lineEdit.setObjectName(u"time_lineEdit")
        self.time_lineEdit.setMinimumSize(QSize(0, 30))
        self.time_lineEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.time_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loadCPU_label = QLabel(self.centralwidget)
        self.loadCPU_label.setObjectName(u"loadCPU_label")
        self.loadCPU_label.setMinimumSize(QSize(150, 0))
        self.loadCPU_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.loadCPU_label)

        self.CPU_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.CPU_plainTextEdit.setObjectName(u"CPU_plainTextEdit")
        self.CPU_plainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.CPU_plainTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.loadRAM_label = QLabel(self.centralwidget)
        self.loadRAM_label.setObjectName(u"loadRAM_label")
        self.loadRAM_label.setMinimumSize(QSize(150, 0))
        self.loadRAM_label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.loadRAM_label)

        self.RAM_plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.RAM_plainTextEdit.setObjectName(u"RAM_plainTextEdit")
        self.RAM_plainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.RAM_plainTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 451, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.time_lineEdit.setText("")
        self.loadCPU_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.loadRAM_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
    # retranslateUi

