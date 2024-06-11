import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt.ViewModels.my_view_model import MyViewModel


class MyView(QWidget):
    def __init__(self, view_model: MyViewModel):
        super().__init__()

        self.setWindowTitle('Counter V')
        self.viewModel = view_model
        self.viewModel.my_signal.connect(self.update_label)

        self.button = QPushButton('Update')
        self.label = QLabel("0")
        self.layout = QVBoxLayout()
        self.__init_ui()

    def __init_ui(self):
        self.layout.addWidget(self.label)

        self.button.clicked.connect(self.viewModel.update_model)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def update_label(self, count):
        self.label.setText(str(count))
