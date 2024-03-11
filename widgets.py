from PyQt6.QtWidgets import QMainWindow, QWidget

from constants import *


class MainWindow(QMainWindow):
    def __init__(self):
        """ Инициализация класса окна приложения"""
        super().__init__()
        self.setFixedSize(WINDOW_WSIZE, WINDOW_HSIZE)  # Фиксированное окно
        # self.setStyleSheet(open("resources/summator_ui.css").read())  # Подключение UI-css файла

        """ Настройка основного виджета"""
        widget = QWidget()
        self.setObjectName("CentralWidget")
        self.setCentralWidget(widget)
