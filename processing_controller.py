'''

Python script to control the user interface for the processing page.
This page is shown whilst the application is processing a rotation request.

'''

# Standard libaray imports
import sys

# PyQt5 imports
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget

# User interface import
from processing_interface import Ui_Form

# Rotator library
import rotator

class Interface(QWidget):
    '''Class for the window shown when application is processing images'''

    def __init__(self, widget : QtWidgets.QStackedWidget):
        '''
        Method to initialise the processing Interface

        Parameters:
            - widget - QStackedWidget used for the application interface
            - parameters - parameters for the execution of the image rotation
        '''

        # Call the super class' constructor
        super(Interface, self).__init__()

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
        self.ui.container.setGraphicsEffect(self.shadow)

        # Hide buttons
        self.ui.button_cancel.setHidden(True)
        self.ui.button_new.setHidden(True)

        # Activate the buttons
        self.ui.button_close.clicked.connect(lambda : sys.exit(1))
        self.ui.button_new.clicked.connect(self.reset)

    def start(self, parameters : dict()):
        '''
        Method to start the execution of the application.
        '''

        # Update the title text
        if len(parameters["files"]) == 1:
            self.ui.label_title.setText("Processing " + str(len(parameters["files"])) + " image")
        else:
            self.ui.label_title.setText("Processing " + str(len(parameters["files"])) + " images")

        # Start the execution of the image rotation
        success = rotator.start(filenames=parameters["files"],
                                             destination=parameters["destination"],
                                             angle=parameters["angle"],
                                             direction=parameters["direction"],
                                             quality=parameters["quality"],
                                             colour=parameters["colour"],
                                             file_extension=parameters["file_extension"],
                                             progress_bar=self.ui.progress_bar,
                                             progress_label=self.ui.label_progress)

        # If the execution was a success, show reset and close buttons
        if success:
            self.ui.button_new.setHidden(False)
            self.ui.button_close.setHidden(False)

        # If the execution was not a success, show the close button only and error message
        else:
            self.ui.button_close.setHidden(False)
            self.ui.label_title.setText("Something went wrong!")
            self.ui.label_title.setStyleSheet("color: rgb(255, 0, 0);")

    def reset(self):
        '''Method to reset the application as if it had been closed and re-opened'''

        # Set the index of the stacked widget to the original index
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

        # Remove all widgets from the stacked widget
        self.widget.removeWidget(self.widget.widget(self.widget.currentIndex()+1))

        # Set the dimensions of the screen
        self.widget.setFixedHeight(590)
        self.widget.setFixedWidth(840)

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.old_position)
        self.widget.move(self.widget.x() + delta.x(), self.widget.y() + delta.y())
        self.old_position = event.globalPos()

def display(widget : QtWidgets.QStackedWidget, parameters : dict()):
    '''
    Method to process the images, and display a screen showing progress

    Parameters:
        - widget - QStackedWidget being used for the application
        - parameters - parameters of the execution in dictionary form
    '''

    # Initialise the processing screen
    screen = Interface(widget)

    # Add the processing screen to the stacked widget
    widget.addWidget(screen)

    # Increment the current index of the stacked widget to display new screen
    widget.setCurrentIndex(widget.currentIndex()+1)

    # Set the dimensions of the new screen
    widget.setFixedHeight(200)
    widget.setFixedWidth(385)

    # Start the execution
    screen.start(parameters)
