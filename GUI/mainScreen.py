import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog


# Main Menu window 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manga reader shit")
        self.resize(800, 600)
        self.main_buttons()

    #Creates button, button size, and functionality for buttons
    def main_buttons(self):
        downloads_button = QPushButton("Downloads", self)
        downloads_button.setGeometry(300, 250, 200, 60)

        #function call for downloads button
        downloads_button.clicked.connect(self.to_download_screen)

        settings_button = QPushButton("Settings", self)
        settings_button.setGeometry(300, 350, 200, 60)

    
    # Increments the current widget index by 1, taking the user to the downloads page
    def to_download_screen(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)


# Downloads window
class downloadWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.downloads_buttons()

    #Creates button to return back to main menu with size, and functionality
    def downloads_buttons(self):
        back2_main = QPushButton("Return to Main", self)
        back2_main.setGeometry(20, 20, 100, 30)

        #function call to bring the user back to the main menu
        back2_main.clicked.connect(self.from_download_screen)

    # Decrements the current widget index by 1, taking the user to the main menu
    def from_download_screen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
 

app = QApplication(sys.argv)

#creates the stack of widgets so the user can change pages without new tabs opening
widget = QtWidgets.QStackedWidget()

main_window = MainWindow()
download_window = downloadWindow()

#Adds the different screens to the stack of widgets
widget.addWidget(main_window)
widget.addWidget(download_window)

widget.resize(800, 600)
widget.show()
sys.exit(app.exec())