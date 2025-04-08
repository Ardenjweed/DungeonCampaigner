from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QCoreApplication

def setup_menuBar(window):
    game_menu = window.menuBar()

    file_menu = game_menu.addMenu("&File")
    quit_action = file_menu.addAction("Quit")
    quit_action.triggered.connect(window.quit_app)

    assets_menu = game_menu.addMenu("Assets")
    image_action = assets_menu.addAction("Import Map")
    image_action.triggered.connect(import_image)
    token_action = assets_menu.addAction("Create Token")
    token_action.triggered.connect(create_token)

def import_image():
    #This is where we would open up the users file directory and ask them to select image
    print("Importing Image")
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.ExistingFile)
    translated_filter = QCoreApplication.translate("QFileDialog", "Images (*.png)")
    dialog.setNameFilter(translated_filter)
    dialog.setViewMode(QFileDialog.List)

    if dialog.exec():
        file_name = dialog.selectedFiles()
        print("The file you picked was: ", file_name)

    

def create_token():
    #This is where we would pop up a QMessageBox where tokens get created
    print("Creating Token")