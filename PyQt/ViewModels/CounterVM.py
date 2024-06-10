from PyQt5.QtCore import QObject, pyqtSignal
from Models import CounterModel


class CounterVM(QObject):
    # signal to update the view
    countChanged = pyqtSignal(int)

    def __init__(self, model: CounterModel.CounterModel):
        super().__init__()
        # reference to the model
        self.model = model

    def increment(self):
        try:
            self.model.increment()
            self.countChanged.emit(self.model.counter)
        except Exception as e:
            print(e)
