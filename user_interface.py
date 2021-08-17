# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 460)
        Form.setStyleSheet("QWidget #Form {\n"
"background-color: rgb(230, 230, 230);\n"
"}")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.label_title.setStyleSheet("font: 18pt \"Gill Sans MT\";")
        self.label_title.setObjectName("label_title")
        self.step_one = QtWidgets.QGroupBox(Form)
        self.step_one.setGeometry(QtCore.QRect(10, 50, 481, 71))
        self.step_one.setStyleSheet("font: 12pt \"Gill Sans MT\";")
        self.step_one.setObjectName("step_one")
        self.button_choose_files = QtWidgets.QPushButton(self.step_one)
        self.button_choose_files.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.button_choose_files.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 255, 255);\n"
"")
        self.button_choose_files.setObjectName("button_choose_files")
        self.label_no_files = QtWidgets.QLabel(self.step_one)
        self.label_no_files.setGeometry(QtCore.QRect(150, 30, 141, 31))
        self.label_no_files.setObjectName("label_no_files")
        self.step_two = QtWidgets.QGroupBox(Form)
        self.step_two.setGeometry(QtCore.QRect(10, 130, 481, 121))
        self.step_two.setStyleSheet("font: 12pt \"Gill Sans MT\";")
        self.step_two.setObjectName("step_two")
        self.ninety_clockwise = QtWidgets.QWidget(self.step_two)
        self.ninety_clockwise.setGeometry(QtCore.QRect(10, 29, 71, 81))
        self.ninety_clockwise.setStyleSheet("QWidget #ninety_clockwise {\n"
"    border-radius : 7px;\n"
"    border-width : 1px;\n"
"    border-style : solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.ninety_clockwise.setObjectName("ninety_clockwise")
        self.label_ninety_clockwise_ninety = QtWidgets.QLabel(self.ninety_clockwise)
        self.label_ninety_clockwise_ninety.setGeometry(QtCore.QRect(0, 40, 71, 31))
        self.label_ninety_clockwise_ninety.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ninety_clockwise_ninety.setObjectName("label_ninety_clockwise_ninety")
        self.label_ninety_clockwise_clockwise = QtWidgets.QLabel(self.ninety_clockwise)
        self.label_ninety_clockwise_clockwise.setGeometry(QtCore.QRect(0, 60, 71, 21))
        self.label_ninety_clockwise_clockwise.setStyleSheet("font: 10pt \"Gill Sans MT\";")
        self.label_ninety_clockwise_clockwise.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ninety_clockwise_clockwise.setObjectName("label_ninety_clockwise_clockwise")
        self.label_ninety_clockwise_arrow = QtWidgets.QLabel(self.ninety_clockwise)
        self.label_ninety_clockwise_arrow.setGeometry(QtCore.QRect(6, 2, 61, 41))
        self.label_ninety_clockwise_arrow.setText("")
        self.label_ninety_clockwise_arrow.setPixmap(QtGui.QPixmap("clockwise.JPG"))
        self.label_ninety_clockwise_arrow.setScaledContents(True)
        self.label_ninety_clockwise_arrow.setObjectName("label_ninety_clockwise_arrow")
        self.ninety_counterclockwise = QtWidgets.QWidget(self.step_two)
        self.ninety_counterclockwise.setGeometry(QtCore.QRect(100, 30, 71, 81))
        self.ninety_counterclockwise.setStyleSheet("QWidget #ninety_counterclockwise {\n"
"    border-radius : 7px;\n"
"    border-width : 1px;\n"
"    border-style : solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.ninety_counterclockwise.setObjectName("ninety_counterclockwise")
        self.label_ninety_counterclockwise_ninety = QtWidgets.QLabel(self.ninety_counterclockwise)
        self.label_ninety_counterclockwise_ninety.setGeometry(QtCore.QRect(0, 40, 71, 31))
        self.label_ninety_counterclockwise_ninety.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ninety_counterclockwise_ninety.setObjectName("label_ninety_counterclockwise_ninety")
        self.label_ninety_counterclockwise_clockwise = QtWidgets.QLabel(self.ninety_counterclockwise)
        self.label_ninety_counterclockwise_clockwise.setGeometry(QtCore.QRect(0, 60, 71, 21))
        self.label_ninety_counterclockwise_clockwise.setStyleSheet("font: 10pt \"Gill Sans MT\";")
        self.label_ninety_counterclockwise_clockwise.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ninety_counterclockwise_clockwise.setObjectName("label_ninety_counterclockwise_clockwise")
        self.label_ninety_counterclockwise_arrow = QtWidgets.QLabel(self.ninety_counterclockwise)
        self.label_ninety_counterclockwise_arrow.setGeometry(QtCore.QRect(6, 2, 61, 41))
        self.label_ninety_counterclockwise_arrow.setText("")
        self.label_ninety_counterclockwise_arrow.setPixmap(QtGui.QPixmap("counter-clockwise.JPG"))
        self.label_ninety_counterclockwise_arrow.setScaledContents(True)
        self.label_ninety_counterclockwise_arrow.setObjectName("label_ninety_counterclockwise_arrow")
        self.onehundredeighty = QtWidgets.QWidget(self.step_two)
        self.onehundredeighty.setGeometry(QtCore.QRect(190, 30, 71, 81))
        self.onehundredeighty.setStyleSheet("QWidget #onehundredeighty {\n"
"    border-radius : 7px;\n"
"    border-width : 1px;\n"
"    border-style : solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.onehundredeighty.setObjectName("onehundredeighty")
        self.label_onehundredeighty_angle = QtWidgets.QLabel(self.onehundredeighty)
        self.label_onehundredeighty_angle.setGeometry(QtCore.QRect(0, 50, 71, 31))
        self.label_onehundredeighty_angle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_onehundredeighty_angle.setObjectName("label_onehundredeighty_angle")
        self.label_onehundredeighty_arrow = QtWidgets.QLabel(self.onehundredeighty)
        self.label_onehundredeighty_arrow.setGeometry(QtCore.QRect(6, 2, 61, 41))
        self.label_onehundredeighty_arrow.setText("")
        self.label_onehundredeighty_arrow.setPixmap(QtGui.QPixmap("half-rotation.JPG"))
        self.label_onehundredeighty_arrow.setScaledContents(True)
        self.label_onehundredeighty_arrow.setObjectName("label_onehundredeighty_arrow")
        self.custom = QtWidgets.QWidget(self.step_two)
        self.custom.setGeometry(QtCore.QRect(280, 30, 71, 81))
        self.custom.setStyleSheet("QWidget #custom {\n"
"    border-radius : 7px;\n"
"    border-width : 1px;\n"
"    border-style : solid;\n"
"    border-color: rgb(0, 0, 0);\n"
"}")
        self.custom.setObjectName("custom")
        self.label_custom = QtWidgets.QLabel(self.custom)
        self.label_custom.setGeometry(QtCore.QRect(0, 0, 71, 81))
        self.label_custom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_custom.setObjectName("label_custom")
        self.clockwise = QtWidgets.QRadioButton(self.step_two)
        self.clockwise.setGeometry(QtCore.QRect(360, 40, 111, 17))
        self.clockwise.setCheckable(True)
        self.clockwise.setChecked(True)
        self.clockwise.setObjectName("clockwise")
        self.counter_clockwise = QtWidgets.QRadioButton(self.step_two)
        self.counter_clockwise.setGeometry(QtCore.QRect(360, 60, 111, 17))
        self.counter_clockwise.setCheckable(True)
        self.counter_clockwise.setObjectName("counter_clockwise")
        self.angle = QtWidgets.QSpinBox(self.step_two)
        self.angle.setGeometry(QtCore.QRect(360, 90, 71, 22))
        self.angle.setMaximum(360)
        self.angle.setObjectName("angle")
        self.step_four = QtWidgets.QGroupBox(Form)
        self.step_four.setGeometry(QtCore.QRect(10, 340, 481, 71))
        self.step_four.setStyleSheet("font: 12pt \"Gill Sans MT\";")
        self.step_four.setObjectName("step_four")
        self.button_choose_destination = QtWidgets.QPushButton(self.step_four)
        self.button_choose_destination.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.button_choose_destination.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 255, 255);\n"
"")
        self.button_choose_destination.setObjectName("button_choose_destination")
        self.label_destination = QtWidgets.QLabel(self.step_four)
        self.label_destination.setGeometry(QtCore.QRect(150, 30, 331, 31))
        self.label_destination.setStyleSheet("font: 8pt \"Gill Sans MT\";")
        self.label_destination.setObjectName("label_destination")
        self.button_start = QtWidgets.QPushButton(Form)
        self.button_start.setGeometry(QtCore.QRect(20, 420, 91, 31))
        self.button_start.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 255, 255);\n"
"font: 14pt \"Gill Sans MT\";")
        self.button_start.setObjectName("button_start")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(130, 420, 211, 31))
        self.progressBar.setStyleSheet("font: 12pt \"Gill Sans MT\";")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_error_success = QtWidgets.QLabel(Form)
        self.label_error_success.setGeometry(QtCore.QRect(350, 420, 141, 31))
        self.label_error_success.setStyleSheet("font: 12pt \"Gill Sans MT\";\n"
"color: rgb(0, 170, 0);")
        self.label_error_success.setObjectName("label_error_success")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 0, 141, 20))
        self.label.setStyleSheet("font: 8pt \"Gill Sans MT\";")
        self.label.setObjectName("label")
        self.step_three = QtWidgets.QGroupBox(Form)
        self.step_three.setGeometry(QtCore.QRect(10, 260, 481, 71))
        self.step_three.setStyleSheet("font: 12pt \"Gill Sans MT\";")
        self.step_three.setObjectName("step_three")
        self.button_same = QtWidgets.QPushButton(self.step_three)
        self.button_same.setGeometry(QtCore.QRect(10, 30, 121, 31))
        self.button_same.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 255, 255);\n"
"")
        self.button_same.setObjectName("button_same")
        self.button_different = QtWidgets.QPushButton(self.step_three)
        self.button_different.setGeometry(QtCore.QRect(150, 30, 121, 31))
        self.button_different.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(85, 255, 255);\n"
"")
        self.button_different.setObjectName("button_different")
        self.percentage_quality = QtWidgets.QSpinBox(self.step_three)
        self.percentage_quality.setGeometry(QtCore.QRect(290, 40, 71, 22))
        self.percentage_quality.setMinimum(10)
        self.percentage_quality.setMaximum(100)
        self.percentage_quality.setProperty("value", 75)
        self.percentage_quality.setObjectName("percentage_quality")
        self.label_percentage = QtWidgets.QLabel(self.step_three)
        self.label_percentage.setGeometry(QtCore.QRect(370, 40, 101, 21))
        self.label_percentage.setStyleSheet("font: 12pt \"Gill Sans MT\";")
        self.label_percentage.setObjectName("label_percentage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "Image Rotator"))
        self.step_one.setTitle(_translate("Form", "Step 1 - Select Image Files"))
        self.button_choose_files.setText(_translate("Form", "Select Files"))
        self.label_no_files.setText(_translate("Form", "0 files chosen"))
        self.step_two.setTitle(_translate("Form", "Step 2 - Choose Rotation"))
        self.label_ninety_clockwise_ninety.setText(_translate("Form", "90°"))
        self.label_ninety_clockwise_clockwise.setText(_translate("Form", "clockwise"))
        self.label_ninety_counterclockwise_ninety.setText(_translate("Form", "90°"))
        self.label_ninety_counterclockwise_clockwise.setText(_translate("Form", "c-clockwise"))
        self.label_onehundredeighty_angle.setText(_translate("Form", "180°"))
        self.label_custom.setText(_translate("Form", "Other"))
        self.clockwise.setText(_translate("Form", "Clockwise"))
        self.counter_clockwise.setText(_translate("Form", "C-Clockwise"))
        self.step_four.setTitle(_translate("Form", "Step 4 - Saving Image Files"))
        self.button_choose_destination.setText(_translate("Form", "Select Location"))
        self.label_destination.setText(_translate("Form", "<location>"))
        self.button_start.setText(_translate("Form", "Start"))
        self.label_error_success.setText(_translate("Form", "Error / Success"))
        self.label.setText(_translate("Form", "Created by: Nicholas Williams"))
        self.step_three.setTitle(_translate("Form", "Step 3 - Choose Quality/File Size Reduction"))
        self.button_same.setText(_translate("Form", "Same Quality"))
        self.button_different.setText(_translate("Form", "Different Quality"))
        self.label_percentage.setText(_translate("Form", "% of Original"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

