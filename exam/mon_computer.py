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
import shutil
import time

import psutil
import pythoncom
import win32com.client
from PySide6 import QtWidgets, QtCore, QtGui

from ui.monitorin_2_ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return:
        """
        self.systemThread.getSystemInfo.connect(self.updSystemInfo)
        self.processThread.getProcessInfo.connect(self.updProcessInfo)
        self.serviceThread.getServiceInfo.connect(self.updServiceInfo)
        self.taskThread.getTaskInfo.connect(self.updTaskInfo)

    def initThreads(self) -> None:
        """
        Инициализация потоков
        :return:
        """
        self.systemThread = SystemInfo()
        self.systemThread.start()
        self.processThread = ProcessInfoThread()
        self.processThread.start()
        self.serviceThread = ServiceInfoThread()
        self.serviceThread.start()
        self.taskThread = TaskInfoThread()
        self.taskThread.start()

    def updSystemInfo(self, system_info):
        """
        Настройка вывода параметров о системе: процессор, ядра, диски и т.д
        :param system_info:
        :return:
        """
        processor, cpu_count, cpu_percent, virtual_memory_total, virtual_memory_percent, \
            disk_partitions, disk_usage_total, disk_usage_used = system_info
        self.ui.process_name_text.appendPlainText(f'{processor}')
        self.ui.cores_count_value.appendPlainText(f'{cpu_count}')
        self.ui.current_load_value.appendPlainText(f'{cpu_percent}')
        self.ui.memory_volume_value.appendPlainText(f'{virtual_memory_total}')
        self.ui.load_memory_value.appendPlainText(f'{virtual_memory_percent}')
        self.ui.disk_count_value.appendPlainText(f'{disk_partitions}')
        self.ui.volume_value.appendPlainText(f'{round(disk_usage_total/10**9, 2)}')
        self.ui.busy_volume_value.appendPlainText(f'{round(disk_usage_used/10**9, 2)}')

    def updProcessInfo(self, data):
        """
        Вывод информации от текущих процессах
        :param data:
        :return:
        """
        self.ui.processplainTextEdit.clear()
        for i in data:
            self.ui.processplainTextEdit.appendPlainText(str(i))

    def updServiceInfo(self, data):
        """
        Вывод информации о службах
        :param data:
        :return:
        """
        self.ui.service_info.clear()
        for i in data:
            self.ui.service_info.appendPlainText(str(i))

    def updTaskInfo(self, data):
        """
        Вывод информации о текущих задачах
        :param data:
        :return:
        """
        self.ui.task_info.clear()
        for i in data:
            self.ui.task_info.appendPlainText(str(i))

    def spinbox_value(self, value):
        """
        Настройка задержки
        :param value:
        :return:
        """
        self.systemThread.delay = value
        self.processThread.delay = value
        self.serviceThread.delay = value
        self.taskThread.delay = value


class SystemInfo(QtCore.QThread):
    getSystemInfo = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = list
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            processor = platform.processor()
            cpu_count = psutil.cpu_count()
            cpu_percent = psutil.cpu_percent()
            virtual_memory_total = psutil.virtual_memory().total
            virtual_memory_percent = psutil.virtual_memory().percent
            disk_partitions = len(psutil.disk_partitions())
            disk_usage = shutil.disk_usage('C:/')
            disk_usage_total = disk_usage.total
            disk_usage_used = disk_usage.used
            self.getSystemInfo.emit([processor, cpu_count, cpu_percent, virtual_memory_total,
                                     virtual_memory_percent, disk_partitions, disk_usage_total, disk_usage_used])
            time.sleep(self.delay)


class ProcessInfoThread(QtCore.QThread):
    getProcessInfo = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {}
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            self.data = psutil.process_iter()
            self.getProcessInfo.emit(self.data)
            time.sleep(self.delay)


class ServiceInfoThread(QtCore.QThread):
    getServiceInfo = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1
        while True:
            self.data = psutil.win_service_iter()
            self.getServiceInfo.emit(self.data)
            time.sleep(self.delay)


class TaskInfoThread(QtCore.QThread):
    getTaskInfo = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 5

        pythoncom.CoInitialize()

        while True:
            scheduler = win32com.client.dynamic.Dispatch('Schedule.Service')
            scheduler.Connect()
            tasks = scheduler.GetRunningTasks(1)
            names = [tasks.Item(i + 1).Name for i in range(tasks.Count)]
            print(names)
            self.getTaskInfo.emit(names)
            time.sleep(self.delay)

    # def closeWindowEvent(self, event: QtGui.QCloseEvent) -> None:
    #     """
    #     Событие закрытия окна
    #     :param event: QtGui.QCloseEvent
    #     :return: None
    #     """
    #
    #     answer = QtWidgets.QMessageBox.question(self, "Закрыть окно?", "Вы действительно хотите закрыть окно?")
    #
    #     if answer == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #         SystemInfo.finished()
    #         ProcessInfoThread.finished()
    #         ServiceInfoThread.finished()
    #     else:
    #         event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()

