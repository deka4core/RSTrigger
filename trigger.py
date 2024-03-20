from PyQt6.QtWidgets import QPushButton, QLabel


class Ports:
    def __init__(self):
        self.reset = False
        self.set = False
        self.clock = False
        self.quit = True

    def get_reset_value(self) -> int:
        return int(self.reset)

    def get_set_value(self) -> int:
        return int(self.set)

    def get_clock_value(self) -> int:
        return int(self.clock)

    def get_quit_value(self) -> int:
        return int(self.quit)

    def get_values(self) -> list:
        return list(map(int, [self.set, self.clock, self.reset, self.quit]))

    def change_port_value(self, port_index: int, labels: list) -> None:
        if port_index == 0:
            self.set = not self.set
        elif port_index == 1:
            self.clock = not self.clock
        else:
            self.reset = not self.reset
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
        labels[0].setStyleSheet(f"background-image:url(./media/label_q_{int(self.get_quit_value())}.png);"
                                "font-size:30px;font-family:'Marske'; color:#0bbaea;")
        labels[1].setText(str(int(not self.get_quit_value())))
        labels[1].setStyleSheet(f"background-image: url(./media/label_q_{int(not self.get_quit_value())}.png);"
                                "font-size:30px;font-family:'Marske';color:#0bbaea;")

    def exception(self, labels: list):
        for i in range(2):
            labels[i].setStyleSheet("background-image: url(./media/label_q_e.png);"
                                    "font-size:30px;font-family:'Marske'; color:#0bbaea;")
            labels[i].setText("E")