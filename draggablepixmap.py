from PySide6.QtWidgets import QGraphicsItem, QGraphicsPixmapItem, QMenu, QDialog
from PySide6.QtGui import QAction
from PySide6.QtGui import QPixmap
from token_creation import TokenCreation

class DraggablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.frozen = False
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        
    def set_frozen(self, frozen):
        self.frozen = frozen
        self.setFlag(QGraphicsItem.ItemIsMovable, not frozen)
        self.setFlag(QGraphicsItem.ItemIsSelectable, not frozen)
        self.setAcceptHoverEvents(not frozen)

    def mousePressEvent(self, event):
        if not self.frozen:
            super().mousePressEvent(event)
        else:
            event.ignore()
        
    def mouseMoveEvent(self, event):
        if not self.frozen:
            super().mouseMoveEvent(event)
        else:
            event.ignore()

class DraggableToken(QGraphicsPixmapItem):
    def __init__(self, pixmap, token):
        super().__init__(pixmap)
        self.token = token
        self._editor = TokenCreation(self.token)  
        self._editor.setModal(True)
        self.frozen = False
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        
    def set_frozen(self, frozen):
        self.frozen = frozen
        self.setFlag(QGraphicsItem.ItemIsMovable, not frozen)
        self.setFlag(QGraphicsItem.ItemIsSelectable, not frozen)
        self.setAcceptHoverEvents(not frozen)

    def mousePressEvent(self, event):
        if not self.frozen:
            super().mousePressEvent(event)
        else:
            event.ignore()
        
    def mouseMoveEvent(self, event):
        if not self.frozen:
            super().mouseMoveEvent(event)
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        menu = QMenu()

        # e.g. rotate action
        rotate_act = QAction("Rotate 90°", menu)
        rotate_act.triggered.connect(lambda: self.setRotation(self.rotation() + 90))
        menu.addAction(rotate_act)

        # delete action
        delete_act = QAction("Delete Token", menu)
        delete_act.triggered.connect(lambda: self.scene().removeItem(self))
        menu.addAction(delete_act)

        # edit action
        edit_act = QAction("Edit", menu)
        edit_act.triggered.connect(self.edit_stats)
        menu.addAction(edit_act)

        # pop up right under the cursor
        menu.exec(event.screenPos())
    
    def edit_stats(self):
        # reload the form with the latest token data
        self._editor._load_token_into_form()

        # show it — reuse the same dialog object each time
        if self._editor.exec() == QDialog.Accepted:
            new_pp = self.token.profile
            if isinstance(new_pp, str):
                self.setPixmap(QPixmap(new_pp))
            elif isinstance(new_pp, QPixmap):
                self.setPixmap(new_pp)
