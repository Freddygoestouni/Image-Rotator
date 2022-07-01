# PyQt5 imports
import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

# Package imports
import main_page_controller

# Open up the app
app = QApplication([])
widget = QtWidgets.QStackedWidget()
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)


# Call the startup page to get the widget
main_page_controller.display(widget)

# Show the start_up
widget.show()

# Other PyQt5 code
try:
    sys.exit(app.exec_())
except:
    sys.exit(1)
