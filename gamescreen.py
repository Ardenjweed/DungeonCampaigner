from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout

class GameScreen(QWidget):
    def __init__(self):
        super().__init__()

        #Random button that we'll get rid of later
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton("Test"))