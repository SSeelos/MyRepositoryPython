from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("MyMainWindow")
        self.setMinimumSize(600, 400)
        self.SetContent()

        self.show()
    def SetContent(self):
        lbl = self.setCentralWidget(QLabel("txt"))
        #btnA = QPushButton("MyButtonA")
        #btnB = QPushButton("MyButtonB")



def Run(args):
    app = QApplication(args)
    window = MainWindow()
    app.exec_()