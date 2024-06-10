from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("MyMainWindow")
        self.setMinimumSize(600, 400)

        self.label = QLabel("myLabel")
        self.button = QPushButton("MyButtonA")
        self.set_layout()
        self.set_interface()

        self.show()


    def set_layout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def set_interface(self):
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("clicked")



def Run(args):
    app = QApplication(args)
    window = MainWindow()
    app.exec_()