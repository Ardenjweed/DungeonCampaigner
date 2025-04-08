from PySide6.QtWidgets import QApplication
import sys
from mainwindow import MainWindow
 
def main():
    app = QApplication(sys.argv) #Essentially sets up application instance

    window = MainWindow(app)
    window.show() #Windows are hidden by default but are shown through this command

    app.exec() #Starts the event loop that keeps application running


if __name__ == "__main__":
    main()