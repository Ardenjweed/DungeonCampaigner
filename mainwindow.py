from PySide6.QtWidgets import QMainWindow, QStackedWidget
from titlescreen import TitleScreen
from gamescreen import GameScreen
from menu_bar import setup_menuBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("DungeonCampaigner")
        self.app = app

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.title_screen = TitleScreen(self)
        self.game_screen = GameScreen()

        #Important to note that index 0 of our stacked widget will be what widget shows up first
        self.stacked_widget.addWidget(self.title_screen)
        self.stacked_widget.addWidget(self.game_screen)

        setup_menuBar(self)
        self.menuBar().setVisible(False)

    def quit_app(self):
        self.app.quit()

    def start_game(self):
        self.stacked_widget.setCurrentWidget(self.game_screen)
        self.menuBar().setVisible(True)
