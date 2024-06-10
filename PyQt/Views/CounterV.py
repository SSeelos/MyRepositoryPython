import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt.ViewModels import CounterVM


class CounterV(QWidget):
    def __init__(self, view_model: CounterVM.CounterVM):
        super().__init__()

        self.setWindowTitle('Counter V')
        self.viewModel = view_model
        self.viewModel.countChanged.connect(self.update_counter)

        self.button = QPushButton('Increment')
        self.label = QLabel("0")
        self.layout = QVBoxLayout()
        self.__init_ui()

    def __init_ui(self):
        self.layout.addWidget(self.label)

        self.button.clicked.connect(self.viewModel.increment)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def update_counter(self, count):
        try:
            self.label.setText(str(count))
        except Exception as e:
            print(e)