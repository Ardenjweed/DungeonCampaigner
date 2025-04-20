from PySide6.QtWidgets import QDialog, QFileDialog, QTextEdit, QMessageBox
from PySide6.QtCore import QCoreApplication, QStandardPaths, QSize
from PySide6.QtGui import QPixmap
#from draggablepixmap import DraggablePixmapItem
from ui_widget import Ui_Dialog


class TokenCreation(QDialog, Ui_Dialog):
    def __init__(self, Token):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Token Sheet")
        icon = QPixmap("Assets/QuestionMark.jpg")
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(200, 200))
        self.token = Token
        self.token.profile = icon
        self.toolButton.clicked.connect(self.set_pfp)
        self.info = self.buttonBox.clicked.connect(self.save_token)
        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.accept)

    def accept(self):
        edits = self.findChildren(QTextEdit)

        optional = { self.desc_textEdit, self.note_textEdit }
        required = [e for e in edits if e not in optional]

        empty = [e for e in required if not e.toPlainText().strip()]
        if empty:
            QMessageBox.warning(
                self,
                "Incomplete Sheet",
                "Please fill in all fields before clicking OK."
            )
            return   # don’t close the dialog
        # if we get here, everything is filled in → save & close
        self.save_token()       
        super().accept()


    def save_token(self):
        self.token.name = self.name_textEdit.toPlainText()
        self.token.description = self.desc_textEdit.toPlainText()
        self.token.initiative = int(self.init_textEdit.toPlainText())
        self.token.health = int(self.hp_textEdit.toPlainText())
        self.token.ac = int(self.ac_textEdit.toPlainText())
        self.token.strength = int(self.str_textEdit.toPlainText())
        self.token.dexterity = int(self.dex_textEdit.toPlainText())
        self.token.constitution = int(self.con_textEdit.toPlainText())
        self.token.intelligence = int(self.int_textEdit.toPlainText())
        self.token.wisdom = int(self.wis_textEdit.toPlainText())
        self.token.charisma = int(self.char_textEdit.toPlainText())
        self.token.notes = self.note_textEdit.toPlainText()

    def set_pfp(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        default_dir = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        dialog.setDirectory(default_dir)
        dialog.setNameFilter(QCoreApplication.translate("QFileDialog", "Images (*.png)"))
        dialog.setViewMode(QFileDialog.List)

        if dialog.exec():
            file_name = dialog.selectedFiles()
            if file_name:
                new_icon = QPixmap(file_name[0])
                self.toolButton.setIcon(new_icon)
                self.toolButton.setIconSize(QSize(200, 200))
                self.token.profile = file_name[0]
