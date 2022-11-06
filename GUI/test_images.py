
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.acceptDrops()
        self.setWindowTitle("Image Testing")
 
        # setting the size of window
        self.setGeometry(0, 0, 400, 300)
 
        # creating label for displaying images
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap('scott_soderquist.jpeg')
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.show()
 
# create pyqt5 app
app = QApplication(sys.argv)
 
# creates the window instance
window = Window()

sys.exit(app.exec())