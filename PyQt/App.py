import sys
from PyQt5.QtWidgets import *

from Models.my_model import MyModel
from PyQt.ViewModels.my_view_model import MyViewModel
from PyQt.Views.my_view import MyView


class MainWindow(QMainWindow):
    view: MyView = None

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("MyMainWindow")
        self.setMinimumSize(600, 400)

        self.label = QLabel("myLabel")
        self.button = QPushButton("MyButtonA")
        self.open_view_btn = QPushButton("OpenView")
        self.layout = QVBoxLayout()
        self.set_layout()
        self.set_interface()

        # self.show()

    def set_layout(self):
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.open_view_btn)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def set_interface(self):
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

        self.open_view_btn.clicked.connect(self.open_view)

    def button_clicked(self):
        print("clicked")

    def open_view(self, checked):
        model = MyModel()
        view_model = MyViewModel(model)

        if self.view is None:
            self.view = MyView(view_model)
        self.view.show()


def run(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
