"""Задача.

Разработать приложение для мониторинга нагрузки системы и системных процессов (аналог диспетчера задач).

Обязательные функции в приложении:

Показ общих сведений о системе (в текстовом виде!):
Название процессора, количество ядер, текущая загрузка
Общий объём оперативной памяти, текущая загрузка оперативаной памяти
Количество, жестких дисков + информация по каждому (общий/занятый объём)
Обеспечить динамический выбор обновления информации (1, 5, 10, 30 сек.)
Показ работающих процессов
Показ работающих служб
Показ задач, которые запускаются с помощью планировщика задач
"""
import platform
import time
import psutil

from PySide6 import QtWidgets, QtCore

from ui.monitorin_2_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        # self.systemThread.getSystemInfo.connect(self.updSystemInfo)
        self.processThread.getProcessInfo.connect(self.updProcessInfo)

    def initThreads(self) -> None:
        # self.systemThread = SystemInfo()
        # self.systemThread.start()
        self.processThread = ProcessInfoThread()
        self.processThread.start()

    # def updSystemInfo(self, data):
    #     self.ui.process_name_text.clear()
    #     self.ui.cores_count_value.clear()
    #     self.ui.current_load_value.clear()
    #     self.ui.memory_volume_value.clear()
    #     self.ui.load_memory_value.clear()
    #     self.ui.disk_count_value.clear()
    #     self.ui.volume_value.clear()
    #     self.ui.busy_volume_value.clear()
    #     for i in data:
    #         self.ui.process_name_text.appendPlainText(str(i.info))
    #         self.ui.cores_count_value.appendPlainText(str(i.info))
    #         self.ui.current_load_value.appendPlainText(str(i.info))
    #         self.ui.memory_volume_value.appendPlainText(str(i.info))
    #         self.ui.load_memory_value.appendPlainText(str(i.info))
    #         self.ui.disk_count_value.appendPlainText(str(i.info))
    #         self.ui.volume_value.appendPlainText(str(i.info))
    #         self.ui.busy_volume_value.appendPlainText(str(i.info))

    def updProcessInfo(self, data):
        self.ui.processplainTextEdit.clear()
        for i in data:
            self.ui.processplainTextEdit.appendPlainText(str(i.info))

    #
    # def ServiceInfo(self, data):
    #     self.ui.service_info.clear()
    #     for i in data:
    #         self.ui.service_info.append(str(i.info))
    #
    # def TaskInfo(self, data):
    #     self.ui.task_info.clear()
    #     for i in data:
    #         self.ui.task_info.appendPlainText(str(i.info))

    def spinbox_value(self, value):
        # self.systemThread.delay = value
        self.processThread.delay = value


# class SystemInfo(QtCore.QThread):
#     getSystemInfo = QtCore.Signal(dict)
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.data = {}
#         self.delay = None
#
#     def run(self) -> None:
#         if self.delay is None:
#             self.delay = 1
#         while True:
#             self.data = platform.processor()
#             self.data = psutil.cpu_count()
#             self.data = psutil.cpu_percent()
#             self.data = psutil.virtual_memory().total
#             self.data = psutil.virtual_memory().percent
#             self.data = psutil.disk_partitions()
#             # self.data = psutil.disk_usage()
#             self.getSystemInfo.emit(self.data)
#             time.sleep(self.delay)


class ProcessInfoThread(QtCore.QThread):
    getProcessInfo = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            self.data = psutil.process_iter()
            self.getProcessInfo.emit(self.data)
            time.sleep(self.delay)


#
# class ServiceInfoThread(QtCore.QThread):
#     getServiceInfo = QtCore.Signal(object)
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.data = None
#         self.delay = None
#
#     def run(self) -> None:
#         if self.delay is None:
#             self.delay = 1
#         while True:
#             self.data = psutil.win_service_iter()
#             self.getServiceInfo.emit(self.data)
#             time.sleep(self.delay)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
