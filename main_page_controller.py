# PyQt5 imports
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap

from main_page_interface import Ui_Form
import rotator
from processing_controller import display as display_processing
from user_guide_controller import display as display_user_gude



# Constants

button_pressed = """
QPushButton{
background-color: rgba(0, 119, 182, 200);
border: 0px solid;
border-radius: 10px;
padding:7px;
}
"""

button_not_pressed = """
QPushButton{
background-color: rgba(202, 240, 248, 200);
border: 0px solid;
border-radius: 10px;
padding:7px;
}
QPushButton:hover{
background-color: rgba(0, 119, 182, 200);
border: 0px solid;
border-radius: 10px;
padding:7px;
}
"""

# User Interface
class Interface(QWidget):
	def __init__(self, widget):
		super(Interface, self).__init__()
		# loadUi("user_interface.ui",self)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.widget = widget


		# Files
		self.files = []
		self.destination = None
		self.rotation = (None, None)    # Direction, Angle
		self.quality = None
		self.alterations = ("Colour", ".jpg")   # Colour, Type

		# Finding the position of the QStackedWidget used in moving the application
		self.old_position = self.widget.pos()

		self.ui.nav_bar_widget.mouseMoveEvent = self.move_screen

		self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))

		self.ui.container_root.setGraphicsEffect(self.shadow)
		self.ui.group_one.setGraphicsEffect(self.shadow)
		self.ui.group_two.setGraphicsEffect(self.shadow)
		self.ui.group_three.setGraphicsEffect(self.shadow)
		self.ui.group_four.setGraphicsEffect(self.shadow)
		self.ui.group_five.setGraphicsEffect(self.shadow)

		# ------------------------------------------------------------------------------------------------------ #
		#       Primary Buttons
		self.ui.button_close.clicked.connect(lambda : sys.exit(1))
		self.ui.button_minimise.clicked.connect(lambda : self.widget.showMinimized())
		self.ui.button_cancel.setHidden(True)
		self.ui.button_user_guide.clicked.connect(lambda : display_user_gude(self.widget))

		# ------------------------------------------------------------------------------------------------------ #
		#       Stage One

		self.ui.button_choose_files.clicked.connect(self.choose_files)

		self.ui.label_no_files.setHidden(True)


		# ------------------------------------------------------------------------------------------------------ #
		#       Stage Two

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


		# ------------------------------------------------------------------------------------------------------ #
		#       Stage Three

		# Choose Quality
		self.ui.button_same_quality.clicked.connect(self.quality_same)
		self.ui.button_different_quality.clicked.connect(self.quality_different)

		self.ui.percentage_quality.valueChanged.connect(self.quality_custom_change)

		self.ui.group_three.setHidden(True)
		self.ui.percentage_quality.setHidden(True)


		# ------------------------------------------------------------------------------------------------------ #
		#       Stage Four

		self.ui.choose_colour.addItems(["Colour", "Black/White"])
		self.ui.choose_file_type.addItems(["Same as Original", ".jpg", ".png"])

		self.ui.choose_colour.activated.connect(self.alterations_colour)
		self.ui.choose_file_type.activated.connect(self.alterations_type)

		self.ui.group_four.setHidden(True)


		# ------------------------------------------------------------------------------------------------------ #
		#       Stage Five

		self.ui.button_choose_save.clicked.connect(self.choose_destination)

		self.ui.group_five.setHidden(True)



		# ------------------------------------------------------------------------------------------------------ #
		#       Business Logic

		self.ui.button_start.setHidden(True)
		self.ui.button_start.clicked.connect(self.start)

		# ------------------------------------------------------------------------------------------------------ #
		#       Preview

		self.ui.container_preview.setHidden(True)
		self.ui.choose_image.activated.connect(self.display_preview)

	def mousePressEvent(self, event):
		self.old_position = event.globalPos()

	def move_screen(self, event):
		delta = QtCore.QPoint(event.globalPos() - self.old_position)
		self.widget.move(self.widget.x() + delta.x(), self.widget.y() + delta.y())
		self.old_position = event.globalPos()


	# Method to handle the selection of the image files
	def choose_files(self):
		# Get File Names
		file_names = QFileDialog.getOpenFileNames(self, 'Choose Image(s)', '', 'Image Files (*.jpg *.png)')

		self.files = file_names[0]

		# Set the number of files label
		if len(self.files) == 1:
			self.ui.label_no_files.setText(str(len(self.files)) + " file chosen")
		else:
			self.ui.label_no_files.setText(str(len(self.files)) + " files chosen")

		self.ui.label_no_files.setHidden(False)

		if len(self.files) > 0:
			self.ui.group_two.setHidden(False)

			# Set up the preview
			short_names = list(map(lambda filename : filename[filename.rindex("/")+1:filename.rindex(".")], self.files))

			self.ui.choose_image.addItems(short_names)

			self.display_preview()


	# --------------------------------------------------------------------------------------------------------- #
	#       Set Rotations

	def rotation_clockwise(self):
		self.rotation = ("Clockwise", self.rotation[1])
		self.ui.button_ninety.setHidden(False)
		self.ui.button_one_eighty.setHidden(False)
		self.ui.button_custom_rotation.setHidden(False)
		self.ui.button_clockwise.setStyleSheet(button_pressed)
		self.ui.button_counter_clockwise.setStyleSheet(button_not_pressed)
		self.display_preview()

	def rotation_counter_clockwise(self):
		self.rotation = ("Counter Clockwise", self.rotation[1])
		self.ui.button_ninety.setHidden(False)
		self.ui.button_one_eighty.setHidden(False)
		self.ui.button_custom_rotation.setHidden(False)
		self.ui.button_counter_clockwise.setStyleSheet(button_pressed)
		self.ui.button_clockwise.setStyleSheet(button_not_pressed)
		self.display_preview()

	def rotation_ninety(self):
		self.rotation = (self.rotation[0], 90)
		self.ui.angle.setHidden(True)
		self.ui.button_ninety.setStyleSheet(button_pressed)
		self.ui.button_one_eighty.setStyleSheet(button_not_pressed)
		self.ui.button_custom_rotation.setStyleSheet(button_not_pressed)

		self.ui.group_three.setHidden(False)
		self.display_preview()

	def rotation_one_eighty(self):
		self.rotation = (self.rotation[0], 180)
		self.ui.angle.setHidden(True)
		self.ui.button_ninety.setStyleSheet(button_not_pressed)
		self.ui.button_one_eighty.setStyleSheet(button_pressed)
		self.ui.button_custom_rotation.setStyleSheet(button_not_pressed)

		self.ui.group_three.setHidden(False)
		self.display_preview()

	def rotation_custom(self):
		self.ui.angle.setHidden(False)
		self.ui.button_ninety.setStyleSheet(button_not_pressed)
		self.ui.button_one_eighty.setStyleSheet(button_not_pressed)
		self.ui.button_custom_rotation.setStyleSheet(button_pressed)

		self.ui.group_three.setHidden(False)
		self.rotation = (self.rotation[0], int(self.ui.angle.value()))
		self.display_preview()

	def rotation_custom_change(self):
		self.rotation = (self.rotation[0], int(self.ui.angle.value()))
		self.display_preview()

	# --------------------------------------------------------------------------------------------------------- #
	#       Set Quality

	def quality_same(self):
		self.quality = 100
		self.ui.button_same_quality.setStyleSheet(button_pressed)
		self.ui.button_different_quality.setStyleSheet(button_not_pressed)
		self.ui.percentage_quality.setHidden(True)

		self.ui.group_four.setHidden(False)
		self.ui.group_five.setHidden(False)
		self.display_preview()

	def quality_different(self):
		self.quality = int(self.ui.percentage_quality.value())
		self.ui.button_same_quality.setStyleSheet(button_not_pressed)
		self.ui.button_different_quality.setStyleSheet(button_pressed)
		self.ui.percentage_quality.setHidden(False)

		self.ui.group_four.setHidden(False)
		self.ui.group_five.setHidden(False)
		self.display_preview()

	def quality_custom_change(self):
		self.quality = int(self.ui.percentage_quality.value())
		self.display_preview()

	# --------------------------------------------------------------------------------------------------------- #
	#       Set Alterations

	def alterations_type(self):
		self.alterations = (self.alterations[0], self.ui.choose_file_type.currentText())
		self.display_preview()

	def alterations_colour(self):
		self.alterations = (self.ui.choose_colour.currentText(), self.alterations[1])
		self.display_preview()

	# --------------------------------------------------------------------------------------------------------- #
	#       Set Destination

	def choose_destination(self):
		# Get Destination
		destination_directory = QFileDialog.getExistingDirectory(self, 'Choose Save Directory')

		self.destination = destination_directory

		if destination_directory is not None:
			self.ui.button_start.setHidden(False)


	# Method to start the business logic
	def start(self):
		parameters = {"files" : self.files,
		                       "destination" : self.destination,
		                       "angle" : self.rotation[1],
		                       "direction" : self.rotation[0],
		                       "quality": self.quality,
		                       "colour" : self.alterations[0],
		                       "file_extension" : self.alterations[1]}

		display_processing(self.widget, parameters)

	def display_preview(self):
		try:
			image_data, w, h = rotator.preview(filename=self.files[self.ui.choose_image.currentIndex()],
			                                                        angle=self.rotation[1],
			                                                        direction=self.rotation[0],
			                                                        quality=self.quality,
			                                                        colour=self.alterations[0])

			q_image = QtGui.QImage(image_data, w, h, QtGui.QImage.Format_ARGB32)

			pixel_map = QtGui.QPixmap.fromImage(q_image)

			pixel_map = pixel_map.scaled(self.ui.image_after.size().width(),
			                                               self.ui.image_after.size().height(),
			                                               QtCore.Qt.KeepAspectRatio,
			                                               QtCore.Qt.SmoothTransformation)

			self.ui.image_after.setPixmap(pixel_map)

			self.ui.container_preview.setHidden(False)
		except:
			pass



# Method to display the user interface
def display(widget):
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
	widget.setFixedHeight(590)#50)
	widget.setFixedWidth(840)#00)
