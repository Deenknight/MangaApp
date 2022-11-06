from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os

class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignCenter)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

    def setImage(self, path):
        self.label.setPixmap(QtGui.QPixmap(path))


class manga_page(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.display()
        self.god = widget

    def display(self):
 
        # creating scroll label
        label = ScrollLabel()
 
        # setting text to the label
        label.setImage(os.path.dirname(__file__)+"\\img.png")
 
        # setting geometry
        label.setGeometry(100, 100, 200, 80)

        self.layout = QVBoxLayout(self)
        

        back2_main = QPushButton("Return to Main", self)
        back2_main.setGeometry(20, 20, 100, 30)

        self.layout.addWidget(back2_main)
        self.layout.addWidget(label)
        back2_main.clicked.connect(self.from_download_screen)

    # Decrements the current widget index by 1, taking the user to the main menu
    def from_download_screen(self):
        self.god.setCurrentIndex(self.god.currentIndex() - 2)
        




