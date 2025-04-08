from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout


class TitleScreen(QWidget):
    def __init__(self, parent):
        super().__init__()

        layout = QVBoxLayout(self)
        button = QPushButton("Start")
        layout.addWidget(button)

        button.clicked.connect(parent.start_game)

        