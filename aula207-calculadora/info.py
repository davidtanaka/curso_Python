from PySide6.QtWidgets import QLabel, QWidget
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        from PySide6.QtCore import Qt
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
