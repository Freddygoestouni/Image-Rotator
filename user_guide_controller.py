import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog

from user_guide_interface import Ui_Form

class User_Guide_Interface(QWidget):
    '''Class for the window shown when application is processing images'''

    def __init__(self, widget : QtWidgets.QStackedWidget):
        '''
        Method to initialise the user guide Interface

        Parameters:
            - widget - QStackedWidget used for the application interface
        '''

        # Call the super class' constructor
        super(User_Guide_Interface, self).__init__()

        # Set up the user interface
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Setting the QStackedWidget
        self.widget = widget

        # Finding the position of the QStackedWidget used in moving the application
        self.old_position = self.widget.pos()

        # Shadow effect
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))

        # Adding shadow to the window
        self.ui.container_root.setGraphicsEffect(self.shadow)

        # Activate the buttons
        self.ui.button_back.clicked.connect(lambda : self.back())
        self.ui.button_close.clicked.connect(lambda : sys.exit(1))
        self.ui.button_minimise.clicked.connect(lambda : self.widget.showMinimized())

    def back(self):
        '''Method to go back to the previous application page'''

        # Set the index of the stacked widget to the original index
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

        # Remove all widgets from the stacked widget
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()+1))

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.old_position)
        self.widget.move(self.widget.x() + delta.x(), self.widget.y() + delta.y())
        self.old_position = event.globalPos()

def display(widget):
    '''
    Method to display the user guide

    Parameters:
        - widget - QStackedWidget being used for the application
    '''

    # Initialise the processing screen
    screen = User_Guide_Interface(widget)

    # Add the processing screen to the stacked widget
    widget.addWidget(screen)

    # Increment the current index of the stacked widget to display new screen
    widget.setCurrentIndex(widget.currentIndex()+1)
