from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QFontDatabase, QFont
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel

from constants import *
from trigger import Ports


class MainWindow(QMainWindow):
    def __init__(self):
        """ Инициализация класса окна приложения"""
        super().__init__()
        self.setFixedSize(WINDOW_WSIZE, WINDOW_HSIZE)  # Фиксированное окно
        self.setStyleSheet(open('style.css').read())

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
            self.buttons.append(QPushButton(self))
            self.buttons[i].setGeometry(MARGIN_LEFT_BGROUP,
                                        MARGIN_TOP_BGROUP + (i * MARGIN_K_BUTTON), BUTTON_WSIZE, BUTTON_HSIZE)
            self.buttons[i].clicked.connect(self.button_clicked)
        self.update_buttons(None)

    def init_labels(self):
        for i in range(2):
            self.labels.append(QLabel('0', self))
            self.labels[i].setGeometry(MARGIN_LEFT_LGROUP, MARGIN_TOP_LGROUP + (i * MARGIN_K_LABEL),
                                       LABEL_WSIZE, LABEL_HSIZE)
            self.labels[i].setAlignment(Qt.AlignmentFlag.AlignCenter)

    def button_clicked(self):
        self.ports.change_port_value(self.buttons.index(self.sender()), self.labels)
        self.update_buttons(self.sender())
        self.update_wires()

    def update_wires(self):
        s, c, r, q = self.ports.get_values()
        if c:
            if s or r:
                self.setStyleSheet("QMainWindow {background-image: " + f" url(./media/rs{s}1{r}.png)" + "}")
            else:
                self.setStyleSheet("QMainWindow {background-image: " + f" url(./media/rs010{q}.png)" + "}")
        else:
            self.setStyleSheet("QMainWindow {background-image: " + f" url(./media/rs{s}0{r}{q}.png)" + "}")

    def update_buttons(self, sender: QPushButton):
        ports = self.ports.get_values()

        if sender:
            index = self.buttons.index(sender)
            pixmap = QPixmap(f"./media/button_{index}_{ports[index]}.png")
            button_icon = QIcon(pixmap)
            sender.setIcon(button_icon)
            sender.setIconSize(pixmap.rect().size())
        else:
            for i in range(3):
                pixmap = QPixmap(f"./media/button_{i}_{ports[i]}.png")
                button_icon = QIcon(pixmap)
                self.buttons[i].setIcon(button_icon)
                self.buttons[i].setIconSize(pixmap.rect().size())
