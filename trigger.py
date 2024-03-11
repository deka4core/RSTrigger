from PyQt6.QtWidgets import QPushButton, QLabel


class Ports:
    def __init__(self):
        self.reset = False
        self.set = False
        self.clock = False
        self.quit = False

    def get_reset_value(self) -> int:
        return int(self.reset)

    def get_set_value(self) -> int:
        return int(self.set)

    def get_clock_value(self) -> int:
        return int(self.clock)

    def get_quit_value(self) -> int:
        return int(self.quit)

    def change_port_value(self, port_index: int, button: QPushButton, labels: list) -> None:
        if port_index == 0:
            self.set = not self.set
            button.setText(str(self.get_set_value()))
        elif port_index == 1:
            self.clock = not self.clock
            button.setText(str(self.get_clock_value()))
        else:
            self.reset = not self.reset
            button.setText(str(self.get_reset_value()))
        self.calculate(labels)

    def calculate(self, labels: list) -> None:
        c, r, s, q = self.clock, self.reset, self.set, self.quit
        self.quit = (c and s) or ((not r) and q) or ((not c) and q)
        if c * r * s == 1:
            self.exception(labels)
        else:
            self.update_labels_text(labels)

    def update_labels_text(self, labels: list) -> None:
        labels[0].setText(str(self.get_quit_value()))
        labels[1].setText(str(int(not self.get_quit_value())))

    def exception(self, labels: list):
        labels[0].setText("Error")
        labels[1].setText("Error")