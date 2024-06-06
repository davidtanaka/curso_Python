import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 150px;')
    return label1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.addWidgeToVLayout(temp_label('label 1'))
    window.addWidgeToVLayout(temp_label('label 2'))
    window.addWidgeToVLayout(temp_label('label 3'))

    window.show()
    app.exec()