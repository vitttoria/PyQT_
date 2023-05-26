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
        self.systemThread.getSystemInfo.connect(self.updSystemInfo)
        self.processThread.getProcessInfo.connect(self.updProcessInfo)
        self.serviceThread.getServiceInfo.connect(self.updServiceInfo)
        self.taskThread.getTaskInfo.connect(self.updTaskInfo)

    def initThreads(self) -> None:
        self.systemThread = SystemInfo()
        self.systemThread.start()
        self.processThread = ProcessInfoThread()
        self.processThread.start()
        self.serviceThread = ServiceInfoThread()
        self.taskThread = TaskInfoThread()
        self.taskThread.start()

    def closeWindowEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        answer = QtWidgets.QMessageBox.question(self, "Закрыть окно?", "Вы действительно хотите закрыть окно?")

        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()
            SystemInfo.finished()
            ProcessInfoThread.finished()
            ServiceInfoThread.finished()
        else:
            event.ignore()

    def updSystemInfo(self, data):
        self.ui.process_name_text.clear()
        self.ui.cores_count_value.clear()
        self.ui.current_load_value.clear()
        self.ui.memory_volume_value.clear()
        self.ui.load_memory_value.clear()
        self.ui.disk_count_value.clear()
        self.ui.volume_value.clear()
        self.ui.busy_volume_value.clear()
        for i in data:
            self.ui.process_name_text.appendPlainText(f'{platform.processor()}')
            self.ui.cores_count_value.appendPlainText(f'{psutil.cpu_count()}')
            self.ui.current_load_value.appendPlainText(f'{psutil.cpu_percent()}')
            self.ui.memory_volume_value.appendPlainText(f'{psutil.virtual_memory().total}')
            self.ui.load_memory_value.appendPlainText(f'{psutil.virtual_memory().percent}')
            self.ui.disk_count_value.appendPlainText(f'{len(psutil.disk_partitions())}')
            self.ui.busy_volume_value.appendPlainText(f'{psutil.disk_usage(i.mountpoint)}')
            pathes = [i.mountpoint for i in psutil.disk_partitions()]
            self.ui.memory_volume_value = \
                [
                    f"{round(psutil.disk_usage(i).total / 1073741824, 2)}"
                    for i in pathes]
            self.ui.load_memory_value = \
                [
                    f"{round(psutil.disk_usage(i).total / 1073741824, 2)}/{round(psutil.disk_usage(i).used / 1073741824, 2)}"
                    for i in pathes]

    def updProcessInfo(self, data):
        self.ui.processplainTextEdit.clear()
        for i in data:
            self.ui.processplainTextEdit.appendPlainText(str(i))

    def updServiceInfo(self, data):
        self.ui.service_info.clear()
        for i in data:
            self.ui.service_info.append(str(i))

    def updTaskInfo(self, data):
        self.ui.task_info.clear()
        for i in data:
            self.ui.task_info.appendPlainText(str(i))

    def spinbox_value(self, value):
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
            self.data = platform.processor()
            self.data = psutil.cpu_count()
            self.data = psutil.cpu_percent()
            self.data = psutil.virtual_memory().total
            self.data = psutil.virtual_memory().percent
            self.data = psutil.disk_partitions()
            pathes = [i.mountpoint for i in psutil.disk_partitions()]
            self.data = \
                [
                    f"{round(psutil.disk_usage(i).total / 1073741824, 2)}" \
                    f"/{round(psutil.disk_usage(i).used / 1073741824, 2)}"
                    for i in pathes]
            self.getSystemInfo.emit(self.data)
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


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = Window()
    window.show()
    app.exec()
