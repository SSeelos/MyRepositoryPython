from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    pass
def Run(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec_()