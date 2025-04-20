from PySide6.QtWidgets import QGraphicsItem, QGraphicsPixmapItem

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