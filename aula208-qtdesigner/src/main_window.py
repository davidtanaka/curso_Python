import sys
from typing import cast

from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.changeLabelResult)  # Use the correct name from UI

        self.lineEdit.installEventFilter(self)  # Use the correct name from UI

    def changeLabelResult(self):
        text = self.lineEdit.text()  # Use the correct name from UI
        self.label.setText(text)  # Use the correct name from UI

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineEdit.text()  # Use the correct name from UI
            self.label.setText(text + event.text())  # Use the correct name from UI

        return super().eventFilter(watched, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()