# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hw_1_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1443, 887)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(924, 705))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_Qt = QAction(MainWindow)
        self.action_Qt.setObjectName(u"action_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1417, 810))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMouseTracking(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton_4 = QRadioButton(self.groupBox_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_5.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_5.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_3)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout_5.addWidget(self.radioButton_6)


        self.horizontalLayout_13.addWidget(self.groupBox_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_4 = QCheckBox(self.groupBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_8.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox_4)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_8.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.groupBox_4)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_8.addWidget(self.checkBox_6)


        self.horizontalLayout_14.addWidget(self.groupBox_4)

        self.horizontalSpacer_4 = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.toolBox_2 = QToolBox(self.tab_3)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 133, 156))
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.page_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_8.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_15.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.page_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_15.addWidget(self.lineEdit_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_16.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.page_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_16.addWidget(self.lineEdit_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_17.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.page_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_17.addWidget(self.lineEdit_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.verticalSpacer_2 = QSpacerItem(20, 194, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.toolBox_2.addItem(self.page_5, u"QLineEdit")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 98, 98))
        self.gridLayout = QGridLayout(self.page_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_2 = QTextEdit(self.page_6)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 0, 0, 1, 1)

        self.toolBox_2.addItem(self.page_6, u"QTextEdit")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 98, 98))
        self.gridLayout_2 = QGridLayout(self.page_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plainTextEdit_2 = QPlainTextEdit(self.page_7)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout_2.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)

        self.toolBox_2.addItem(self.page_7, u"QPlainTextEdit")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 667, 551))
        self.gridLayout_3 = QGridLayout(self.page_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.calendarWidget_2 = QCalendarWidget(self.page_8)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")

        self.gridLayout_3.addWidget(self.calendarWidget_2, 0, 0, 1, 1)

        self.toolBox_2.addItem(self.page_8, u"QCalendarWidget")

        self.horizontalLayout_12.addWidget(self.toolBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_5 = QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_18.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.tab_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_18.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.tab_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_18.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.tab_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_18.addWidget(self.pushButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 0, 1347, 744))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 90, 291, 231))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(160, 0))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setMinimumSize(QSize(0, 0))
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_4)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setMinimumSize(QSize(0, 0))
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_5.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.groupBox_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setMinimumSize(QSize(0, 0))
        self.lineEdit_9.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_9)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(330, 90, 341, 231))
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_6.addWidget(self.label_10)

        self.textEdit = QTextEdit(self.groupBox_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.textEdit)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_7.addWidget(self.label_11)

        self.textEdit_3 = QTextEdit(self.groupBox_5)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.textEdit_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_9.addWidget(self.label_12)

        self.textEdit_4 = QTextEdit(self.groupBox_5)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.textEdit_4)


        self.gridLayout_5.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_10.addWidget(self.label_13)

        self.textEdit_5 = QTextEdit(self.groupBox_5)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.textEdit_5)


        self.gridLayout_5.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_11.addWidget(self.label_14)

        self.textEdit_6 = QTextEdit(self.groupBox_5)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.textEdit_6)


        self.gridLayout_5.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(680, 90, 621, 231))
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget = QTableWidget(self.groupBox_6)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 249, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush1);
        __qtablewidgetitem8.setForeground(brush);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        brush2 = QBrush(QColor(0, 255, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setBackground(brush2);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        brush3 = QBrush(QColor(0, 255, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setBackground(brush3);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(930, 330, 371, 181))
        self.gridLayout_7 = QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.progressBar = QProgressBar(self.groupBox_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(24)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.progressBar)


        self.gridLayout_7.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_20.addWidget(self.label_16)

        self.progressBar_2 = QProgressBar(self.groupBox_7)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(70)
        self.progressBar_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_20.addWidget(self.progressBar_2)


        self.gridLayout_7.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_21.addWidget(self.label_17)

        self.progressBar_3 = QProgressBar(self.groupBox_7)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMaximum(100)
        self.progressBar_3.setValue(100)
        self.progressBar_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_21.addWidget(self.progressBar_3)


        self.gridLayout_7.addLayout(self.horizontalLayout_21, 2, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(930, 510, 391, 211))
        self.gridLayout_10 = QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_2 = QPushButton(self.groupBox_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(70, 70))
        self.pushButton_2.setMaximumSize(QSize(70, 70))
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(70, 70))
        self.pushButton_3.setMaximumSize(QSize(70, 70))
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(70, 70))
        self.pushButton_4.setMaximumSize(QSize(70, 70))
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.pushButton_4)


        self.gridLayout_10.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_2 = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.groupBox_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(70, 70))
        self.pushButton.setMaximumSize(QSize(70, 70))

        self.horizontalLayout_27.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)


        self.gridLayout_10.addLayout(self.horizontalLayout_27, 0, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(30, 560, 881, 161))
        self.gridLayout_9 = QGridLayout(self.groupBox_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalSlider = QSlider(self.groupBox_10)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.horizontalSlider)

        self.label_22 = QLabel(self.groupBox_10)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_9.addWidget(self.label_22)


        self.gridLayout_9.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalSlider_2 = QSlider(self.groupBox_10)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.horizontalSlider_2)

        self.label_23 = QLabel(self.groupBox_10)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_10.addWidget(self.label_23)


        self.gridLayout_9.addLayout(self.verticalLayout_10, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSlider_3 = QSlider(self.groupBox_10)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.horizontalSlider_3)

        self.label_24 = QLabel(self.groupBox_10)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_11.addWidget(self.label_24)


        self.gridLayout_9.addLayout(self.verticalLayout_11, 0, 2, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalSlider_4 = QSlider(self.groupBox_10)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.horizontalSlider_4)

        self.label_25 = QLabel(self.groupBox_10)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_12.addWidget(self.label_25)


        self.gridLayout_9.addLayout(self.verticalLayout_12, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(131, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalSlider_5 = QSlider(self.groupBox_10)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.horizontalSlider_5)

        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_13.addWidget(self.label_26)


        self.gridLayout_9.addLayout(self.verticalLayout_13, 0, 5, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(30, 340, 881, 211))
        self.gridLayout_8 = QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_18 = QLabel(self.groupBox_9)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_23.addWidget(self.label_18)

        self.textEdit_7 = QTextEdit(self.groupBox_9)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.textEdit_7)


        self.gridLayout_8.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_19 = QLabel(self.groupBox_9)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_24.addWidget(self.label_19)

        self.textEdit_8 = QTextEdit(self.groupBox_9)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.textEdit_8)


        self.gridLayout_8.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_20 = QLabel(self.groupBox_9)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_25.addWidget(self.label_20)

        self.textEdit_9 = QTextEdit(self.groupBox_9)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.textEdit_9)


        self.gridLayout_8.addLayout(self.horizontalLayout_25, 2, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.groupBox_9)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_26.addWidget(self.label_21)

        self.textEdit_10 = QTextEdit(self.groupBox_9)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.textEdit_10)


        self.gridLayout_8.addLayout(self.horizontalLayout_26, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_11.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1443, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_Qt)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox_2.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"QRadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton 1", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"RadioButton 2", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"RadioButton 3", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"QCheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0443 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0438\u043c\u044f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"QLineEdit", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043f\u043e\u043b\u0443\u0436\u0438\u0440\u043d\u044b\u043c</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-style:italic;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043a\u0443\u0440\u0441\u0438\u0432\u043e\u043c.</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br />\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u043d\u043e </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; text-decoration: underline;\">\u043f\u043e\u0434\u0447\u0435\u0440\u043a\u043d\u0443\u0442\u044c</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; vertical-align:super;\">\u043d\u0430"
                        "\u0434\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u043c</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">\u0422\u0435\u043a\u0441\u0442 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; vertical-align:sub;\">\u043f\u043e\u0434\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u043c</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">.</span></p></body></html>", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in semper nulla, sed feugiat turpis. Cras blandit suscipit pharetra. Aliquam vitae mollis magna. Curabitur a tortor nec risus venenatis vehicula. Proin a metus eu arcu tempus iaculis ut sed dui. Sed bibendum convallis tellus, eu viverra arcu pulvinar sit amet. Proin vitae lorem in tellus imperdiet rhoncus sed eget elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec efficitur molestie elit ac facilisis. Morbi ac volutpat dui, ut scelerisque lectus. Nunc dapibus eros sem, vitae molestie augue bibendum eu. Ut neque diam, ornare eu ligula eget, sagittis faucibus augue. Mauris tristique volutpat porta. Nunc eget nulla in leo viverra mattis. Proin malesuada enim quis scelerisque finibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"QCalendarWidget", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u043e\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u041a\u0410", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043e\u0440\u0431\u0438\u0442\u044b", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"10256 \u043a\u043c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"0,2 \u043c/\u0441", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u041a\u0410", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"364 \u043a\u043c/\u0447", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>22</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"60,00000", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"30,00000", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff9300;\">22 \u0441</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0435\u0441\u0441", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442 3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"36,6", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"140/70", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"36,8", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"120/60", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"36,5", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"130/70", None));
        ___qtablewidgetitem14 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043f\u043b\u0438\u0432\u043e", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u043d\u0435\u0432\u0440\u043e\u0432\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u2193", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff9300;\">\u0412\u043d\u0438\u043c\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.textEdit_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00f900;\">\u041d\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

