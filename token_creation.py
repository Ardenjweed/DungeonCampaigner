from PySide6.QtWidgets import QDialog
from ui_widget import Ui_Dialog

class TokenCreation(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Token Sheet")
        self.buttonBox.clicked.connect(self.save_token)


    def save_token(self):
        print("WIP")
