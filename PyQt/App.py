from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    button: QPushButton
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("MyMainWindow")
        self.setMinimumSize(600, 400)

        self.label = QLabel("myLabel")
        self.set_layout()

        self.show()
    def set_layout(self):

        self.button = QPushButton("MyButtonA")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def button_clicked(self):
        print("clicked")



def Run(args):
    app = QApplication(args)
    window = MainWindow()
    app.exec_()