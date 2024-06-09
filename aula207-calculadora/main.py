import sys
from main_window import MainWindow
from info import Info
from display import Display
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from buttons import ButtonsGrid
from styles import setupTheme

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    

    # Condição para aparecer o ícone na barra de tarefas (windows).
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')
         # Arbitrary string 

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()