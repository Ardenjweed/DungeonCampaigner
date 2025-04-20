from PySide6.QtWidgets import (QWidget, QGraphicsScene, QGraphicsView, QFileDialog, 
                               QTextEdit, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import QCoreApplication, QPoint, Qt, QStandardPaths
from PySide6.QtGui import QPixmap, QWheelEvent, QMouseEvent
from draggablepixmap import DraggablePixmapItem, DraggableToken
from tokenpiece import Token

class GameScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-1_000_000, -1_000_000, 2_000_000, 2_000_000)
        
        self.view = CustomGraphicsView(self.scene)
        self.view.setMinimumWidth(500)
        self.view.setDragMode(QGraphicsView.NoDrag)
        self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.text_edit = QTextEdit()
        self.text_edit.setMinimumWidth(200)

        main_layout = QHBoxLayout(self)
        view_layout = QVBoxLayout()
        view_layout.addWidget(self.view)
        main_layout.addLayout(view_layout)  
        main_layout.addWidget(self.text_edit)

        self._pan_start = QPoint()
    
    def import_image(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        default_dir = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        dialog.setDirectory(default_dir)
        dialog.setNameFilter(QCoreApplication.translate("QFileDialog", "Images (*.png)"))
        dialog.setViewMode(QFileDialog.List)

        if dialog.exec():
            file_name = dialog.selectedFiles()
            if file_name:
                self.add_image_to_scene(file_name[0], 0)

    def add_image_to_scene(self, file_path, typ):
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            pixmap_item = None
            if typ == 0:
                pixmap_item = DraggablePixmapItem(pixmap)
                pixmap_item.setZValue(-1)
            elif typ == 1:
                pixmap_item = DraggableToken(pixmap)
                pixmap_item.setZValue(1)
            self.scene.addItem(pixmap_item)
            scene_center = self.scene.sceneRect().center()
            item_center = pixmap_item.boundingRect().center()
            pixmap_item.setPos(scene_center - item_center)
            self.view.centerOn(scene_center)

    def freeze_all_maps(self, freeze=True):
        """Toggle freeze state for all maps"""
        for item in self.scene.items():
            if isinstance(item, DraggablePixmapItem):
                item.set_frozen(freeze)
    
    def freeze_all_tokens(self, freeze=True):
        """Toggle freeze state for all tokens"""
        for item in self.scene.items():
            if isinstance(item, DraggableToken):
                item.set_frozen(freeze)

    def create_token(self):
        token = Token()
        pfp = token.get_pfp()
        self.add_image_to_scene(pfp, 1)

class CustomGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self._is_panning = False

    def wheelEvent(self, event: QWheelEvent):
        zoom_factor = 1.1
        if event.angleDelta().y() > 0:
            self.scale(zoom_factor, zoom_factor)
        else:
            self.scale(1/zoom_factor, 1/zoom_factor)
        event.accept()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            pos = event.position().toPoint()
            item = self.itemAt(pos)
                
            # Check if we clicked on a frozen item or no item
            if (isinstance(item, (DraggablePixmapItem, DraggableToken)) and item.frozen) or not item:
                self.setDragMode(QGraphicsView.ScrollHandDrag)
                self._is_panning = True
            else:
                self.setDragMode(QGraphicsView.NoDrag)
                
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton and self._is_panning:
            self.setDragMode(QGraphicsView.NoDrag)
            self._is_panning = False
        super().mouseReleaseEvent(event)

def setup_menuBar(window):
    game_menu = window.menuBar()
    
    # File menu
    file_menu = game_menu.addMenu("&File")
    quit_action = file_menu.addAction("Quit")
    quit_action.triggered.connect(window.quit_app)
    
    # Assets menu
    assets_menu = game_menu.addMenu("Assets")
    image_action = assets_menu.addAction("Import Map")
    image_action.triggered.connect(lambda _: window.game_screen.import_image())

    token_creation = assets_menu.addAction("Create Token")
    token_creation.triggered.connect(window.game_screen.create_token)
    
    # New freeze menu
    freeze_menu = game_menu.addMenu("&Tools")
    freeze_bg_action = freeze_menu.addAction("Freeze All Backgrounds")
    freeze_bg_action.triggered.connect(lambda: window.game_screen.freeze_all_maps(True))
    unfreeze_bg_action = freeze_menu.addAction("Unfreeze All Backgrounds")
    unfreeze_bg_action.triggered.connect(lambda: window.game_screen.freeze_all_maps(False))

    freeze_token_action = freeze_menu.addAction("Freeze All Tokens")
    freeze_token_action.triggered.connect(lambda: window.game_screen.freeze_all_tokens(True))
    unfreeze_token_action = freeze_menu.addAction("Unfreeze All Tokens")
    unfreeze_token_action.triggered.connect(lambda: window.game_screen.freeze_all_tokens(False))
