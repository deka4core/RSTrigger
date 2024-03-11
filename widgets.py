from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel

from constants import *
from trigger import Ports


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

        self.ports = Ports()

        self.buttons = []
        self.init_buttons()

        self.labels = []
        self.init_labels()
        self.ports.update_labels_text(self.labels)

    def init_buttons(self):
        for i in range(3):
            self.buttons.append(QPushButton('0', self))
            self.buttons[i].setGeometry(MARGIN_LEFT_BGROUP,
                                        MARGIN_TOP_BGROUP + (i * MARGIN_K_BUTTON), BUTTON_WSIZE, BUTTON_HSIZE)
            self.buttons[i].clicked.connect(self.button_clicked)

    def init_labels(self):
        for i in range(2):
            self.labels.append(QLabel('0', self))
            self.labels[i].setGeometry(MARGIN_LEFT_LGROUP, MARGIN_TOP_LGROUP + (i * MARGIN_K_LABEL),
                                       LABEL_WSIZE, LABEL_HSIZE)

    def button_clicked(self):
        self.ports.change_port_value(self.buttons.index(self.sender()), self.sender(), self.labels)
