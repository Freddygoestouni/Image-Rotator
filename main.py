# PyQt5 imports
import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

# Package imports
import interface

# Open up the app
app = QApplication([])
widget = QtWidgets.QStackedWidget()


# Call the startup page to get the widget
interface.display(widget)

# Show the start_up
widget.show()

# Other PyQt5 code
try:
    sys.exit(app.exec_())
except:
    sys.exit(1)
