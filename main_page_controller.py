'''

Python script to control the user interface for the main page (input page) of the application.
This page is shown whilst the application is gathering user input and previewing the results.

'''

# Standard libaray imports
import sys
import os

# PyQt5 imports
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap

# User interface import
from main_page_interface import Ui_Form

# Other application pages imports
from processing_controller import display as display_processing
from user_guide_controller import display as display_user_gude

# Rotator library
import rotator

# Stylesheet for a pressed button
button_pressed = """
								QPushButton{
									background-color : rgba(0, 119, 182, 200);
									border : 0px solid;
									border-radius : 10px;
									padding : 7px;
								}
							"""

# Stylesheet for a button not pressed
button_not_pressed = """
										QPushButton{
											background-color : rgba(202, 240, 248, 200);
											border : 0px solid;
											border-radius : 10px;
											padding : 7px;
										}
										QPushButton:hover{
											background-color : rgba(0, 119, 182, 200);
											border : 0px solid;
											border-radius : 10px;
											padding : 7px;
										}
									"""

class Interface(QWidget):
	'''Class for the window shown when application is gathering user input'''

	def __init__(self, widget : QtWidgets.QStackedWidget):
		'''
        Method to initialise the primary Interface

        Parameters:
            - widget - QStackedWidget used for the application interface
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

		# Set the navigation bar to be able to move the screen
		self.ui.nav_bar_widget.mouseMoveEvent = self.move_screen

		# Shadow effect
		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))

		# Adding shadow to the window and group boxes
		self.ui.container_root.setGraphicsEffect(self.shadow)
		self.ui.group_one.setGraphicsEffect(self.shadow)
		self.ui.group_two.setGraphicsEffect(self.shadow)
		self.ui.group_three.setGraphicsEffect(self.shadow)
		self.ui.group_four.setGraphicsEffect(self.shadow)
		self.ui.group_five.setGraphicsEffect(self.shadow)

		# User input for the parameters of execution
		self.files = list()
		self.destination = None
		self.rotation = (None, None)    # Direction, Angle
		self.quality = None
		self.alterations = ("Colour", "Same as Original")   # Colour, Type

		# Activate navigation bar buttons
		self.ui.button_user_guide.clicked.connect(lambda : display_user_gude(self.widget))
		self.ui.button_minimise.clicked.connect(lambda : self.widget.showMinimized())
		self.ui.button_close.clicked.connect(lambda : sys.exit(1))

		# Manage stage one components
		self.ui.button_choose_files.clicked.connect(self.choose_files)

		# Manage stage two components
		self.ui.group_two.setHidden(True)
		self.ui.button_clockwise.clicked.connect(self.rotation_clockwise)
		self.ui.button_counter_clockwise.clicked.connect(self.rotation_counter_clockwise)
		self.ui.button_ninety.setHidden(True)
		self.ui.button_one_eighty.setHidden(True)
		self.ui.button_custom_rotation.setHidden(True)
		self.ui.angle.setHidden(True)
		self.ui.button_ninety.clicked.connect(self.rotation_ninety)
		self.ui.button_one_eighty.clicked.connect(self.rotation_one_eighty)
		self.ui.button_custom_rotation.clicked.connect(self.rotation_custom)
		self.ui.angle.valueChanged.connect(self.rotation_custom_change)

		# Manage stage three components
		self.ui.group_three.setHidden(True)
		self.ui.button_same_quality.clicked.connect(self.quality_same)
		self.ui.button_different_quality.clicked.connect(self.quality_different)
		self.ui.percentage_quality.valueChanged.connect(self.quality_custom_change)
		self.ui.percentage_quality.setHidden(True)

		# Manage stage four components
		self.ui.group_four.setHidden(True)
		self.ui.choose_colour.addItems(["Colour", "Black/White"])
		self.ui.choose_file_type.addItems(["Same as Original", ".jpg", ".png"])
		self.ui.choose_colour.activated.connect(self.alterations_colour)
		self.ui.choose_file_type.activated.connect(self.alterations_type)

		# Manage stage five components
		self.ui.group_five.setHidden(True)
		self.ui.button_choose_save.clicked.connect(self.choose_destination)

		# Manage preview components
		self.ui.container_preview.setHidden(True)
		self.ui.choose_image.activated.connect(self.display_preview)

		# Manage execution components
		self.ui.button_start.setHidden(True)
		self.ui.button_start.clicked.connect(self.start)

	def mousePressEvent(self, event):
		self.old_position = event.globalPos()

	def move_screen(self, event):
		delta = QtCore.QPoint(event.globalPos() - self.old_position)
		self.widget.move(self.widget.x() + delta.x(), self.widget.y() + delta.y())
		self.old_position = event.globalPos()

	# Method to handle the selection of the image files
	def choose_files(self):
		'''
		Method for the user to select image files for processing.
		'''

		# Desktop location
		desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

		# Get file paths via file explorer dialog
		file_names = QFileDialog.getOpenFileNames(self, 'Choose Image(s)', desktop, 'Image Files (*.jpg *.png)')

		# Set the file paths class variable
		self.files = file_names[0]

		# Update the label detailing the number of files chosen
		if len(self.files) == 1:
			self.ui.label_no_files.setText(str(len(self.files)) + " file chosen")
		else:
			self.ui.label_no_files.setText(str(len(self.files)) + " files chosen")

		# Only if the user has selected any files, go to next stage
		if len(self.files) > 0:
			# Un-hide the next stage
			self.ui.group_two.setHidden(False)

			# Set up the preview by finding the file names
			short_names = list(map(lambda filename : filename[filename.rindex("/")+1:filename.rindex(".")], self.files))
			self.ui.choose_image.addItems(short_names)
			self.display_preview()

	def rotation_clockwise(self):
		'''
		Method to handle what happens when the clockwise button is pressed
		'''

		# Update the user input saved
		self.rotation = ("Clockwise", self.rotation[1])

		# Un-hide angle buttons
		self.ui.button_ninety.setHidden(False)
		self.ui.button_one_eighty.setHidden(False)
		self.ui.button_custom_rotation.setHidden(False)

		# Update the styles of the direction buttons
		self.ui.button_clockwise.setStyleSheet(button_pressed)
		self.ui.button_counter_clockwise.setStyleSheet(button_not_pressed)

		# Update the preview being displayed
		self.display_preview()

	def rotation_counter_clockwise(self):
		'''
		Method to handle what happens when the counter clockwise button is pressed
		'''

		# Update the user input saved
		self.rotation = ("Counter Clockwise", self.rotation[1])

		# Un-hide angle buttons
		self.ui.button_ninety.setHidden(False)
		self.ui.button_one_eighty.setHidden(False)
		self.ui.button_custom_rotation.setHidden(False)

		# Update the styles of the direction buttons
		self.ui.button_counter_clockwise.setStyleSheet(button_pressed)
		self.ui.button_clockwise.setStyleSheet(button_not_pressed)

		# Update the preview being displayed
		self.display_preview()

	def rotation_ninety(self):
		'''
		Method to handle what happens when the 90° button is pressed
		'''

		# Update the user input saved
		self.rotation = (self.rotation[0], 90)

		# Hide the specific angle chooser
		self.ui.angle.setHidden(True)

		# Update the styles of the angles buttons
		self.ui.button_ninety.setStyleSheet(button_pressed)
		self.ui.button_one_eighty.setStyleSheet(button_not_pressed)
		self.ui.button_custom_rotation.setStyleSheet(button_not_pressed)

		# Show the stage 3 user input
		self.ui.group_three.setHidden(False)

		# Update the preview being displayed
		self.display_preview()

	def rotation_one_eighty(self):
		'''
		Method to handle what happens when the 180° button is pressed
		'''

		# Update the user input saved
		self.rotation = (self.rotation[0], 180)

		# Hide the specific angle chooser
		self.ui.angle.setHidden(True)

		# Update the styles of the angles buttons
		self.ui.button_ninety.setStyleSheet(button_not_pressed)
		self.ui.button_one_eighty.setStyleSheet(button_pressed)
		self.ui.button_custom_rotation.setStyleSheet(button_not_pressed)

		# Show the stage 3 user input
		self.ui.group_three.setHidden(False)

		# Update the preview being displayed
		self.display_preview()

	def rotation_custom(self):
		'''
		Method to handle what happens when the ?° button is pressed
		'''

		# Update the user input saved
		self.rotation = (self.rotation[0], int(self.ui.angle.value()))

		# Hide the specific angle chooser
		self.ui.angle.setHidden(False)

		# Update the styles of the angles buttons
		self.ui.button_ninety.setStyleSheet(button_not_pressed)
		self.ui.button_one_eighty.setStyleSheet(button_not_pressed)
		self.ui.button_custom_rotation.setStyleSheet(button_pressed)

		# Show the stage 3 user input
		self.ui.group_three.setHidden(False)

		# Update the preview being displayed
		self.display_preview()

	def rotation_custom_change(self):
		'''
		Method to handle what happens when the user changes the custom rotation angle
		'''

		# Update the user input saved
		self.rotation = (self.rotation[0], int(self.ui.angle.value()))

		# Update the preview being displayed
		self.display_preview()

	def quality_same(self):
		'''
		Method to handle what happens when the user chooses to keep the same image quality
		'''

		# Update the user input saved
		self.quality = 100

		# Update the styles of the quality buttons
		self.ui.button_same_quality.setStyleSheet(button_pressed)
		self.ui.button_different_quality.setStyleSheet(button_not_pressed)

		# Hide the percentage quality chooser
		self.ui.percentage_quality.setHidden(True)

		# Show the stage 4 and 5 interfaces
		self.ui.group_four.setHidden(False)
		self.ui.group_five.setHidden(False)

		# Update the preview being displayed
		self.display_preview()

	def quality_different(self):
		'''
		Method to handle what happens when the user chooses to change the image quality
		'''

		# Update the user input saved
		self.quality = int(self.ui.percentage_quality.value())

		# Update the styles of the quality buttons
		self.ui.button_same_quality.setStyleSheet(button_not_pressed)
		self.ui.button_different_quality.setStyleSheet(button_pressed)

		# Show the percentage quality chooser
		self.ui.percentage_quality.setHidden(False)

		# Show the stage 4 and 5 interfaces
		self.ui.group_four.setHidden(False)
		self.ui.group_five.setHidden(False)

		# Update the preview being displayed
		self.display_preview()

	def quality_custom_change(self):
		'''
		Method to handle what happens when the user changes the specific image quality
		'''

		# Update the user input saved
		self.quality = int(self.ui.percentage_quality.value())

		# Update the preview being displayed
		self.display_preview()

	def alterations_type(self):
		'''
		Method to handle what happens when the user changes the file extension to be saved as
		'''

		# Update the user input saved
		self.alterations = (self.alterations[0], self.ui.choose_file_type.currentText())

		# Update the preview being displayed
		self.display_preview()

	def alterations_colour(self):
		'''
		Method to handle what happens when the user changes the colour space
		'''

		# Update the user input saved
		self.alterations = (self.ui.choose_colour.currentText(), self.alterations[1])

		# Update the preview being displayed
		self.display_preview()

	def choose_destination(self):
		'''
		Method to handle what happens when the user presses the choose destination button
		'''

		# Get Destination
		destination_directory = QFileDialog.getExistingDirectory(self, 'Choose Save Directory')

		# Update the user input saved
		self.destination = destination_directory

		# If the user has chosen a valid destination, show the start processing button
		if destination_directory is not None:
			self.ui.button_start.setHidden(False)

	def start(self):
		'''
		Method to handle what happens when the user starts the processing of the images
		'''

		# Package the parameters from the user input into a dictionary
		parameters = {"files" : self.files,
		                       "destination" : self.destination,
		                       "angle" : self.rotation[1],
		                       "direction" : self.rotation[0],
		                       "quality": self.quality,
		                       "colour" : self.alterations[0],
		                       "file_extension" : self.alterations[1]}

		# Show the processing interface which also starts the processing itself
		display_processing(self.widget, parameters)

	def display_preview(self):
		'''
		Method to handle creating a preview of the current selected image
		'''

		try:
			# Call the preview method with the given parameters and current selected image
			image_data, w, h = rotator.preview(filename=self.files[self.ui.choose_image.currentIndex()],
			                                                        angle=self.rotation[1],
			                                                        direction=self.rotation[0],
			                                                        quality=self.quality,
			                                                        colour=self.alterations[0])

			# Convert the image to a QImage to be shown
			q_image = QtGui.QImage(image_data, w, h, QtGui.QImage.Format_ARGB32)

			# Convert the QImage to a QPixmap to be shown
			pixel_map = QtGui.QPixmap.fromImage(q_image)

			# Scale the QPixmap to the size of the preview box
			pixel_map = pixel_map.scaled(self.ui.image_after.size().width(),
			                                               self.ui.image_after.size().height(),
			                                               QtCore.Qt.KeepAspectRatio,
			                                               QtCore.Qt.SmoothTransformation)

			# Show the QPixmap in the preview box
			self.ui.image_after.setPixmap(pixel_map)

			# Show the preview container
			self.ui.container_preview.setHidden(False)
		except:
			pass


def display(widget : QtWidgets.QStackedWidget):
	'''
	Method to display the main screen of the application and gather user input

	Parameters:
		- widget - QStackedWidget being used for the application
	'''

	# Initialise the main screen
	screen = Interface(widget)

	# Add the screen to the stacked widget
	widget.addWidget(screen)

	# Set the dimensions of the screen
	widget.setFixedHeight(590)
	widget.setFixedWidth(840)
