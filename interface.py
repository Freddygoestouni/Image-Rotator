# PyQt5 imports
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap

import rotator

# User Interface
class Interface(QWidget):
    def __init__(self, widget):
        super(Interface, self).__init__()
        loadUi("user_interface.ui",self)

        # Files
        self.files = []
        self.destination = None
        self.rotation = None
        self.quality = None

        # ------------------------------------------------------------------------------------------------------ #
        #       Stage One

        # Choose File
        self.button_choose_files.clicked.connect(self.choose_files)

        self.label_no_files.setHidden(True)


        # ------------------------------------------------------------------------------------------------------ #
        #       Stage Two

        self.ninety_clockwise.mouseReleaseEvent = self.option1
        self.ninety_counterclockwise.mouseReleaseEvent = self.option2
        self.onehundredeighty.mouseReleaseEvent = self.option3
        self.custom.mouseReleaseEvent = self.option4

        self.angle.valueChanged.connect(self.customChange)
        self.clockwise.toggled.connect(self.customChange)
        self.counter_clockwise.toggled.connect(self.customChange)

        self.step_two.setHidden(True)
        self.clockwise.setHidden(True)
        self.counter_clockwise.setHidden(True)
        self.angle.setHidden(True)

        # ------------------------------------------------------------------------------------------------------ #
        #       Stage Three

        # Choose Quality
        self.button_same.clicked.connect(self.same_quality)
        self.button_different.clicked.connect(self.different_quality)

        self.percentage_quality.valueChanged.connect(self.qualityChange)

        self.step_three.setHidden(True)
        self.percentage_quality.setHidden(True)
        self.label_percentage.setHidden(True)


        # ------------------------------------------------------------------------------------------------------ #
        #       Stage Four

        self.button_choose_destination.clicked.connect(self.choose_destination)

        self.label_destination.setHidden(True)
        self.step_four.setHidden(True)


        # ------------------------------------------------------------------------------------------------------ #
        #       Business Logic

        # Start Rotation
        self.button_start.clicked.connect(self.start_rotations)

        self.button_start.setHidden(True)
        self.progressBar.setHidden(True)
        self.label_error_success.setHidden(True)



    # Method to handle the selection of the image files
    def choose_files(self):
        # Get File Names
        file_names = QFileDialog.getOpenFileNames(self, 'Choose Image(s)', '', 'Image Files (*.jpg *.png)')

        self.files = file_names[0]

        # Set the number of files label
        self.label_no_files.setText(str(len(self.files)) + " files chosen")
        self.label_no_files.setHidden(False)

        if len(self.files) > 0:
            self.step_two.setHidden(False)


    # --------------------------------------------------------------------------------------------------------- #
    #       Set Rotations


    def option1(self, irrelevant):
        self.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")
        self.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")

        self.clockwise.setHidden(True)
        self.counter_clockwise.setHidden(True)
        self.angle.setHidden(True)

        self.rotation = 90
        self.step_three.setHidden(False)

    def option2(self, irrelevant):
        self.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")
        self.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")

        self.clockwise.setHidden(True)
        self.counter_clockwise.setHidden(True)
        self.angle.setHidden(True)

        self.rotation = 270
        self.step_three.setHidden(False)

    def option3(self, irrelevant):
        self.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")
        self.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")

        self.clockwise.setHidden(True)
        self.counter_clockwise.setHidden(True)
        self.angle.setHidden(True)

        self.rotation = 180
        self.step_three.setHidden(False)

    def option4(self, irrelevant):
        self.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.onehundredeighty.setStyleSheet("QWidget #onehundredeighty { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(0, 0, 0); }")
        self.custom.setStyleSheet("QWidget #custom { border-radius : 7px; border-width : 1px; border-style : solid; border-color: rgb(85, 255, 255); }")

        self.clockwise.setHidden(False)
        self.counter_clockwise.setHidden(False)
        self.angle.setHidden(False)

        if self.clockwise.isChecked():
            self.rotation = int(self.angle.value())
        else:
            self.rotation = 360 - int(self.angle.value())
        self.step_three.setHidden(False)

    def customChange(self):
        if self.clockwise.isChecked():
            self.rotation = int(self.angle.value())
        else:
            self.rotation = 360 - int(self.angle.value())


    # Method to handle the selection of the destination folder
    def choose_destination(self):
        # Get Destination
        destination_directory = QFileDialog.getExistingDirectory(self, 'Choose Save Directory')

        self.destination = destination_directory

        self.label_destination.setText(self.destination)
        self.label_destination.setHidden(False)

        if destination_directory is not None:
            self.button_start.setHidden(False)


    # Method for same quality
    def same_quality(self):
        self.quality = 100
        self.percentage_quality.setHidden(True)
        self.label_percentage.setHidden(True)
        self.step_four.setHidden(False)

    # Method for different quality
    def different_quality(self):
        self.quality = int(self.percentage_quality.value())
        self.percentage_quality.setHidden(False)
        self.label_percentage.setHidden(False)
        self.step_four.setHidden(False)

    # Method for if the quality selection is to be changed
    def qualityChange(self):
        self.quality = int(self.percentage_quality.value())

    # Method to start the business logic
    def start_rotations(self):
        self.label_error_success.setHidden(True)
        self.progressBar.setHidden(False)
        self.progressBar.setValue(0)

        success = rotator.start(self.files, self.rotation, self.quality, self.destination, self.progressBar)

        if success:
            self.label_error_success.setText("Success!")
            self.label_error_success.setStyleSheet("color: rgb(0, 170, 0);")
        else:
            self.label_error_success.setText("Something went wrong!")
            self.label_error_success.setStyleSheet("color: rgb(255, 0, 0);")

        self.label_error_success.setHidden(False)




# Method to display the user interface
def display(widget):
    screen = Interface(widget)
    widget.addWidget(screen)
    widget.setFixedHeight(460)
    widget.setFixedWidth(500)
