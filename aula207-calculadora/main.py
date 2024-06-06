import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('Minha calculadora')
    label1.setStyleSheet('font-size: 75px;')
    window.v_layout.addWidget(label1)
    window.adjustFixedSize()


    label1 = QLabel('O meu texto')
    window.show()
    app.exec()