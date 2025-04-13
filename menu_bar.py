from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QFileDialog, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QCoreApplication, QPoint
from PySide6.QtGui import QPixmap, QWheelEvent

class GameScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-1_000_000, -1_000_000, 2_000_000, 2_000_000) #Setting up infinite canvas space
        
        self.view = CustomGraphicsView(self.scene)
        self.view.setMinimumWidth(500)
        #Settting up ability to drag image around and zoom in/out
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.text_edit = QTextEdit()
        self.text_edit.setMinimumWidth(200)

        main_layout = QHBoxLayout(self)

        view_layout = QVBoxLayout()
        view_layout.addWidget(self.view)
        
        main_layout.addLayout(view_layout)  
        main_layout.addWidget(self.text_edit) 

        # Panning variables
        self._pan_start = QPoint()
    
    def import_image(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        translated_filter = QCoreApplication.translate("QFileDialog", "Images (*.png)")
        dialog.setNameFilter(translated_filter)
        dialog.setViewMode(QFileDialog.List)

        if dialog.exec():
            file_name = dialog.selectedFiles()
            print("The file you picked was: ", file_name)

        if file_name:
            file_name = file_name[0]
            pixmap = QPixmap(file_name)
            self.scene.clear()

            pixmap_item = self.scene.addPixmap(pixmap)
            scene_center = self.scene.sceneRect().center()
            item_center = pixmap_item.boundingRect().center()
            pixmap_item.setPos(scene_center - item_center)
            self.view.centerOn(scene_center)

class CustomGraphicsView(QGraphicsView):
    def wheelEvent(self, event: QWheelEvent):
        zoom_factor = 1.1
        if event.angleDelta().y() > 0:
            self.scale(zoom_factor, zoom_factor)
        else:
            self.scale(1/zoom_factor, 1/zoom_factor)
        event.accept() 


def setup_menuBar(window):
    game_menu = window.menuBar()

    file_menu = game_menu.addMenu("&File")
    quit_action = file_menu.addAction("Quit")
    quit_action.triggered.connect(window.quit_app)

    assets_menu = game_menu.addMenu("Assets")
    image_action = assets_menu.addAction("Import Map")
    image_action.triggered.connect(lambda _: window.game_screen.import_image())
    token_action = assets_menu.addAction("Create Token")
    token_action.triggered.connect(create_token)


def create_token():
    #This is where we would pop up a QMessageBox where tokens get created
    print("Creating Token")