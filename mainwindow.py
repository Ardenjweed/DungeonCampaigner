from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from titlescreen import TitleScreen
from gamescreen import setup_menuBar, GameScreen

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("DungeonCampaigner")
        self.app = app

        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()

        aspect_ratio = 16 / 9

        window_width = int(screen_width * 0.8)  # For example, 80% of screen width
        window_height = int(window_width / aspect_ratio)

        self.resize(window_width, window_height)

        self.move(
            (screen_width - window_width) // 2,
            (screen_height - window_height) // 2
        )

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
