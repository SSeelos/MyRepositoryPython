from PyQt5.QtCore import QObject, pyqtSignal
from Models.my_model import MyModel


class MyViewModel(QObject):
    # signal to update the view
    my_signal = pyqtSignal(int)

    def __init__(self, model: MyModel):
        super().__init__()
        # reference to the model
        self.model = model

    def update_model(self):
        try:
            self.model.update_data()
            # emit signal to transfer data
            self.my_signal.emit(self.model.data)
        except Exception as e:
            print(e)
