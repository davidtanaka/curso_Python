import sys
from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.addToVLayout(display)

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