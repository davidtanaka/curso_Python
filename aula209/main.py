from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_Form
import sys
from time import sleep

class Worker1(QObject):
    started = progressed = finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit('0')
        for i in range(5):
            value = str(i)
            self.progressed.emit(str(i))
            sleep(1)
            self.finished.emit(value)

class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hardWork1) # type: ignore
        self.pushButton_2.clicked.connect(self.hardWork2) # type: ignore

    def hardWork1(self):
        self.label.setText('Trabalho 1 Finalizado')

    def hardWork2(self):
        self.label_2.setText('Trabalho 2 Finalizado')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()