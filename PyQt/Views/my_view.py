import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt.ViewModels.my_view_model import MyViewModel


class MyView(QWidget):
    def __init__(self, view_model: MyViewModel):
        super().__init__()
        # reference to the view model
        self.viewModel = view_model
        # connect slot (fct) to signal
        self.viewModel.my_signal.connect(self.update_label)

        self.setWindowTitle('MyView')

        self.button = QPushButton('Update')
        self.label = QLabel("0")
        self.layout = QVBoxLayout()
        self.__init_ui()

    def __init_ui(self):
        self.layout.addWidget(self.label)

        self.button.clicked.connect(self.viewModel.update_model)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    # function that can be used as a slot
    def update_label(self, data):
        self.label.setText(str(data))
