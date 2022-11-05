import sys

from PyQt5.QtWidgets import QApplication, QDesktopWidget

# main function should just start the app and run the window
app = QApplication(sys.argv)
sizeObject = QDesktopWidget().screenGeometry(-1) # -1 denotes current screen
window = mainScreen() #FIXME needs a mainScreen
window.show() # always run at the end
sys.exit(app.exec_())