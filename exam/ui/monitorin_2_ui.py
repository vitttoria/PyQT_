# class Ui_MainWindow(object):
    # def setupUi(self, MainWindow):
    #     if not MainWindow.objectName():
    #         MainWindow.setObjectName(u"MainWindow")
    #     MainWindow.resize(866, 653)
    #     self.centralwidget = QWidget(MainWindow)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monitorin_2_uiPGzRYH.ui'
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
    QLabel, QMainWindow, QMenuBar, QPlainTextEdit,
    QScrollArea, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QWidget)
from PySide6 import QtWidgets, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.computer_tabwidget = QTabWidget(self.centralwidget)
        self.computer_tabwidget.setObjectName(u"computer_tabwidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_9 = QGridLayout(self.tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 792, 464))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.process_group = QGroupBox(self.scrollAreaWidgetContents_2)
        self.process_group.setObjectName(u"process_group")
        self.gridLayout_6 = QGridLayout(self.process_group)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.process_name = QLabel(self.process_group)
        self.process_name.setObjectName(u"process_name")
        self.process_name.setMinimumSize(QSize(280, 0))
        self.process_name.setMaximumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.process_name)

        self.process_name_text = QPlainTextEdit(self.process_group)
        self.process_name_text.setObjectName(u"process_name_text")
        self.process_name_text.setMaximumSize(QSize(16777215, 30))
        self.process_name_text.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.process_name_text)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cores_count = QLabel(self.process_group)
        self.cores_count.setObjectName(u"cores_count")
        self.cores_count.setMinimumSize(QSize(280, 0))
        self.cores_count.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_11.addWidget(self.cores_count)

        self.cores_count_value = QPlainTextEdit(self.process_group)
        self.cores_count_value.setObjectName(u"cores_count_value")
        self.cores_count_value.setMaximumSize(QSize(16777215, 30))
        self.cores_count_value.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.cores_count_value)


        self.gridLayout_6.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.current_load = QLabel(self.process_group)
        self.current_load.setObjectName(u"current_load")
        self.current_load.setMinimumSize(QSize(280, 0))
        self.current_load.setMaximumSize(QSize(16777215, 30))
        self.current_load.setBaseSize(QSize(0, 0))

        self.horizontalLayout_12.addWidget(self.current_load)

        self.current_load_value = QPlainTextEdit(self.process_group)
        self.current_load_value.setObjectName(u"current_load_value")
        self.current_load_value.setMaximumSize(QSize(16777215, 30))
        self.current_load_value.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.current_load_value)


        self.gridLayout_6.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.process_group, 0, 0, 1, 1)

        self.memory_group = QGroupBox(self.scrollAreaWidgetContents_2)
        self.memory_group.setObjectName(u"memory_group")
        self.gridLayout_7 = QGridLayout(self.memory_group)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.memory_volume = QLabel(self.memory_group)
        self.memory_volume.setObjectName(u"memory_volume")
        self.memory_volume.setMinimumSize(QSize(280, 30))
        self.memory_volume.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_13.addWidget(self.memory_volume)

        self.memory_volume_value = QPlainTextEdit(self.memory_group)
        self.memory_volume_value.setObjectName(u"memory_volume_value")
        self.memory_volume_value.setMaximumSize(QSize(16777215, 30))
        self.memory_volume_value.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.memory_volume_value)


        self.gridLayout_7.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.memory_load_2 = QLabel(self.memory_group)
        self.memory_load_2.setObjectName(u"memory_load_2")
        self.memory_load_2.setMinimumSize(QSize(280, 0))
        self.memory_load_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_14.addWidget(self.memory_load_2)

        self.load_memory_value = QPlainTextEdit(self.memory_group)
        self.load_memory_value.setObjectName(u"load_memory_value")
        self.load_memory_value.setMaximumSize(QSize(16777215, 30))
        self.load_memory_value.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.load_memory_value)


        self.gridLayout_7.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.memory_group, 1, 0, 1, 1)

        self.hard_disk = QGroupBox(self.scrollAreaWidgetContents_2)
        self.hard_disk.setObjectName(u"hard_disk")
        self.gridLayout_8 = QGridLayout(self.hard_disk)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.disk_count = QLabel(self.hard_disk)
        self.disk_count.setObjectName(u"disk_count")
        self.disk_count.setMinimumSize(QSize(280, 0))
        self.disk_count.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_15.addWidget(self.disk_count)

        self.disk_count_value = QPlainTextEdit(self.hard_disk)
        self.disk_count_value.setObjectName(u"disk_count_value")
        self.disk_count_value.setMaximumSize(QSize(16777215, 30))
        self.disk_count_value.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.disk_count_value)


        self.gridLayout_8.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.volume = QLabel(self.hard_disk)
        self.volume.setObjectName(u"volume")
        self.volume.setMinimumSize(QSize(280, 0))
        self.volume.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_16.addWidget(self.volume)

        self.volume_value = QPlainTextEdit(self.hard_disk)
        self.volume_value.setObjectName(u"volume_value")
        self.volume_value.setMaximumSize(QSize(16777215, 30))
        self.volume_value.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.volume_value)


        self.gridLayout_8.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.busy_volume_2 = QLabel(self.hard_disk)
        self.busy_volume_2.setObjectName(u"busy_volume_2")
        self.busy_volume_2.setMinimumSize(QSize(280, 0))
        self.busy_volume_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_17.addWidget(self.busy_volume_2)

        self.busy_volume_value = QPlainTextEdit(self.hard_disk)
        self.busy_volume_value.setObjectName(u"busy_volume_value")
        self.busy_volume_value.setMaximumSize(QSize(16777215, 30))
        self.busy_volume_value.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.busy_volume_value)


        self.gridLayout_8.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.hard_disk, 2, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_9.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.timer_2 = QLabel(self.tab)
        self.timer_2.setObjectName(u"timer_2")
        self.timer_2.setMinimumSize(QSize(400, 0))
        self.timer_2.setMaximumSize(QSize(1000000, 30))

        self.horizontalLayout_18.addWidget(self.timer_2)

        self.spinBox = QSpinBox(self.tab)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(30)

        self.horizontalLayout_18.addWidget(self.spinBox)


        self.gridLayout_9.addLayout(self.horizontalLayout_18, 1, 0, 1, 1)

        self.computer_tabwidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.processplainTextEdit = QPlainTextEdit(self.tab_2)
        self.processplainTextEdit.setObjectName(u"processplainTextEdit")
        self.processplainTextEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.processplainTextEdit, 0, 0, 1, 1)

        self.computer_tabwidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.service_info = QTextEdit(self.tab_3)
        self.service_info.setObjectName(u"service_info")
        self.service_info.setReadOnly(True)

        self.gridLayout_4.addWidget(self.service_info, 0, 0, 1, 1)

        self.computer_tabwidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.tab_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 792, 480))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.task_info = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.task_info.setObjectName(u"task_info")
        self.task_info.setReadOnly(True)

        self.gridLayout_2.addWidget(self.task_info, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.computer_tabwidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.computer_tabwidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 864, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.computer_tabwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.process_group.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.process_name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430:", None))
        self.cores_count.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044f\u0434\u0435\u0440:", None))
        self.current_load.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430, %:", None))
        self.memory_group.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.memory_volume.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u043e\u0431\u044a\u0435\u043c \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0439 \u043f\u0430\u043c\u044f\u0442\u0438:", None))
        self.memory_load_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0439 \u043f\u0430\u043c\u044f\u0442\u0438, %:", None))
        self.hard_disk.setTitle(QCoreApplication.translate("MainWindow", u"\u0416\u0435\u0441\u0442\u043a\u0438\u0435 \u0434\u0438\u0441\u043a\u0438", None))
        self.disk_count.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0436\u0435\u0441\u0442\u043a\u0438\u0445 \u0434\u0438\u0441\u043a\u043e\u0432:", None))
        self.volume.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u043e\u0431\u044a\u0435\u043c:", None))
        self.busy_volume_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u044b\u0439 \u043e\u0431\u044a\u0435\u043c:", None))
        self.timer_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0435\u0440 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.computer_tabwidget.setTabText(self.computer_tabwidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.computer_tabwidget.setTabText(self.computer_tabwidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.computer_tabwidget.setTabText(self.computer_tabwidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0431\u044b", None))
        self.computer_tabwidget.setTabText(self.computer_tabwidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
    # retranslateUi


