# PyQt5 imports
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap

from user_interface import Ui_Form
from getResource import resource_path
import rotator
import pkgutil


# User Interface


class Interface(QWidget):
    def __init__(self, widget):
        super(Interface, self).__init__()
        # loadUi("user_interface.ui",self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Files
        self.files = []
        self.destination = None
        self.rotation = None
        self.quality = None

        # ------------------------------------------------------------------------------------------------------ #
        #       Stage One

        # Choose File
        self.ui.button_choose_files.clicked.connect(self.choose_files)

        self.ui.label_no_files.setHidden(True)


        # ------------------------------------------------------------------------------------------------------ #
        #       Stage Two

        self.ui.ninety_clockwise.mouseReleaseEvent = self.option1
        self.ui.ninety_counterclockwise.mouseReleaseEvent = self.option2
        self.ui.onehundredeighty.mouseReleaseEvent = self.option3
        self.ui.custom.mouseReleaseEvent = self.option4

        self.ui.angle.valueChanged.connect(self.customChange)
        self.ui.clockwise.toggled.connect(self.customChange)
        self.ui.counter_clockwise.toggled.connect(self.customChange)

        self.ui.step_two.setHidden(True)
        self.ui.clockwise.setHidden(True)
        self.ui.counter_clockwise.setHidden(True)
        self.ui.angle.setHidden(True)

        image1 = resource_path("clockwise.jpg")
        image2 = resource_path("counter-clockwise.jpg")
        image3 = resource_path("half-rotation.jpg")

        self.ui.label_ninety_clockwise_arrow.setPixmap(QtGui.QPixmap(image1))
        self.ui.label_ninety_counterclockwise_arrow.setPixmap(QtGui.QPixmap(image2))
        self.ui.label_onehundredeighty_arrow.setPixmap(QtGui.QPixmap(image3))

        # ------------------------------------------------------------------------------------------------------ #
        #       Stage Three

        # Choose Quality
        self.ui.button_same.clicked.connect(self.same_quality)
        self.ui.button_different.clicked.connect(self.different_quality)

        self.ui.percentage_quality.valueChanged.connect(self.qualityChange)

        self.ui.step_three.setHidden(True)
        self.ui.percentage_quality.setHidden(True)
        self.ui.label_percentage.setHidden(True)


        # ------------------------------------------------------------------------------------------------------ #
        #       Stage Four

        self.ui.button_choose_destination.clicked.connect(self.choose_destination)

        self.ui.label_destination.setHidden(True)
        self.ui.step_four.setHidden(True)


        # ------------------------------------------------------------------------------------------------------ #
        #       Business Logic

        # Start Rotation
        self.ui.button_start.clicked.connect(self.start_rotations)

        self.ui.button_start.setHidden(True)
        self.ui.progressBar.setHidden(True)
        self.ui.label_error_success.setHidden(True)



    # Method to handle the selection of the image files
    def choose_files(self):
        # Get File Names
        file_names = QFileDialog.getOpenFileNames(self, 'Choose Image(s)', '', 'Image Files (*.jpg *.png)')

        self.files = file_names[0]

        # Set the number of files label
        self.ui.label_no_files.setText(str(len(self.files)) + " files chosen")
        self.ui.label_no_files.setHidden(False)

        if len(self.files) > 0:
            self.ui.step_two.setHidden(False)


    # --------------------------------------------------------------------------------------------------------- #
    #       Set Rotations


    def option1(self, irrelevant):
        self.ui.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")
        self.ui.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")

        self.ui.clockwise.setHidden(True)
        self.ui.counter_clockwise.setHidden(True)
        self.ui.angle.setHidden(True)

        self.rotation = 90
        self.ui.step_three.setHidden(False)

    def option2(self, irrelevant):
        self.ui.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")
        self.ui.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")

        self.ui.clockwise.setHidden(True)
        self.ui.counter_clockwise.setHidden(True)
        self.ui.angle.setHidden(True)

        self.rotation = 270
        self.ui.step_three.setHidden(False)

    def option3(self, irrelevant):
        self.ui.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")
        self.ui.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")

        self.ui.clockwise.setHidden(True)
        self.ui.counter_clockwise.setHidden(True)
        self.ui.angle.setHidden(True)

        self.rotation = 180
        self.ui.step_three.setHidden(False)

    def option4(self, irrelevant):
        self.ui.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ui.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")

        self.ui.clockwise.setHidden(False)
        self.ui.counter_clockwise.setHidden(False)
        self.ui.angle.setHidden(False)

        if self.ui.clockwise.isChecked():
            self.rotation = int(self.ui.angle.value())
        else:
            self.rotation = 360 - int(self.ui.angle.value())
        self.ui.step_three.setHidden(False)

    def customChange(self):
        if self.ui.clockwise.isChecked():
            self.rotation = int(self.ui.angle.value())
        else:
            self.rotation = 360 - int(self.ui.angle.value())


    # Method to handle the selection of the destination folder
    def choose_destination(self):
        # Get Destination
        destination_directory = QFileDialog.getExistingDirectory(self, 'Choose Save Directory')

        self.destination = destination_directory

        self.ui.label_destination.setText(self.destination)
        self.ui.label_destination.setHidden(False)

        if destination_directory is not None:
            self.ui.button_start.setHidden(False)


    # Method for same quality
    def same_quality(self):
        self.quality = 100
        self.ui.percentage_quality.setHidden(True)
        self.ui.label_percentage.setHidden(True)
        self.ui.step_four.setHidden(False)

    # Method for different quality
    def different_quality(self):
        self.quality = int(self.ui.percentage_quality.value())
        self.ui.percentage_quality.setHidden(False)
        self.ui.label_percentage.setHidden(False)
        self.ui.step_four.setHidden(False)

    # Method for if the quality selection is to be changed
    def qualityChange(self):
        self.quality = int(self.ui.percentage_quality.value())

    # Method to start the business logic
    def start_rotations(self):
        self.ui.label_error_success.setHidden(True)
        self.ui.progressBar.setHidden(False)
        self.ui.progressBar.setValue(0)

        success = rotator.start(self.files, self.rotation, self.quality, self.destination, self.ui.progressBar)

        if success:
            self.ui.label_error_success.setText("Success!")
            self.ui.label_error_success.setStyleSheet("color: rgb(0, 170, 0);")
        else:
            self.ui.label_error_success.setText("Something went wrong!")
            self.ui.label_error_success.setStyleSheet("color: rgb(255, 0, 0);")

        self.ui.label_error_success.setHidden(False)




# Method to display the user interface
def display(widget):
    screen = Interface(widget)
    widget.addWidget(screen)
    widget.setFixedHeight(460)
    widget.setFixedWidth(500)
