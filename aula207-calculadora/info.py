from PySide6.QtWidgets import QLabel, QWidget
from variables import SMALL_FONT_SIZE

# Classe para mostrar as contas em cima do display
class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        from PySide6.QtCore import Qt
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
