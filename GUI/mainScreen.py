import sys
from PyQt5 import QtWidgets
#import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manga reader shit")
        self.resize(800, 600)

        self.main_buttons()


    def main_buttons(self):
        downloads_button = QPushButton("Downloads", self)
        downloads_button.setGeometry(300, 250, 200, 60)
        downloads_button.clicked.connect(self.to_download_screen)

        settings_button = QPushButton("Settings", self)
        settings_button.setGeometry(300, 350, 200, 60)

        
    def to_download_screen(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    

        
class downloadWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.downloads_buttons()

    def downloads_buttons(self):
        back2_main = QPushButton("Return to Main", self)
        back2_main.setGeometry(20, 20, 100, 30)
        back2_main.clicked.connect(self.from_download_screen)

    def from_download_screen(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = MainWindow()

download_window = downloadWindow()
widget.addWidget(main_window)
widget.addWidget(download_window)
widget.resize(800, 600)
widget.show()
sys.exit(app.exec())