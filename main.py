'''

Python script to run the image rotator application. This can either run or package the application.

The script can compile the .ui files from Qt Designer into .py files for use by the application.
If this is not done after the .ui files are modified, these modifications will not be carried through
when the application is run. This uses pyuic5 to convert.

The script can package the application. This uses PyInstaller and will create the executable in
the folder '/dist'.

To run this python script enter the following command into the command window:

            python main.py                                          - to simply run the application

            python main.py --compile                           - to compile the .ui files and run the application

            python main.py --compile --no-run             - to compile the .ui files only

            python main.py --package --no-run            - to package the application

'''

# Standard Libaray Imports
import sys
import os
import subprocess
import argparse
import PyInstaller.__main__
from appdirs import user_data_dir
import shutil
import winshell

# PyQt5 imports
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

# User Interface Imports
import main_page_controller

# Arguments of the execution
parser = argparse.ArgumentParser()
parser.add_argument("--compile",
                                  help="Compile the .ui user interface files before executing",
                                  action=argparse.BooleanOptionalAction)
parser.add_argument("--package",
                                  help="Package the application to an executable",
                                  action=argparse.BooleanOptionalAction)
parser.add_argument("--install",
                                  help="Installs the application and creates desktop shortcut (only use with --package)",
                                  action=argparse.BooleanOptionalAction)
parser.add_argument("--run",
                                  help="Run the application",
                                  default=True,
                                  action=argparse.BooleanOptionalAction)
args = parser.parse_args()

if args.compile:
    # Compile the user interface files (*.ui)
    subprocess.run(["pyuic5", "main_page_interface.ui", "-o", "main_page_interface.py"])
    subprocess.run(["pyuic5", "processing_interface.ui", "-o", "processing_interface.py"])
    subprocess.run(["pyuic5", "user_guide_interface.ui", "-o", "user_guide_interface.py"])

if args.package:
    # Package the application
    PyInstaller.__main__.run([
        '--noconfirm',
        'main.spec',
    ])

    if args.install:
        # Create an application files directory
        app_data_directory = os.path.join(user_data_dir(), 'ImageRotator')
        if not os.path.exists(app_data_directory):
            os.makedirs(app_data_directory)

        # Copy the application executable to the directory
        shutil.copy(os.path.join("dist", "Image Rotator.exe"), app_data_directory)

        # Create the shortcut on the desktop
        with winshell.shortcut(os.path.join(os.environ['USERPROFILE'], 'Desktop', "Image Rotator.lnk")) as link:
            link.path = os.path.join(app_data_directory, "Image Rotator.exe")
            link.description = "Image Rotator"

        # Create a shortcut in the apps list
        with winshell.shortcut(os.path.join(os.environ["userprofile"], "Start Menu", "Programs", "Image Rotator.lnk")) as link:
            link.path = os.path.join(app_data_directory, "Image Rotator.exe")
            link.description = "Image Rotator"

if args.run:
    # Start the application
    app = QApplication([])

    # Create a stacked widget for the user interface
    widget = QtWidgets.QStackedWidget()

    # Remove the frame and make the background transluscent
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Call the main page user interface to be displayed on the application stacked widget
    main_page_controller.display(widget)

    # Show the application interface
    widget.show()

    # Other PyQt5 code
    try:
        sys.exit(app.exec_())
    except:
        sys.exit(1)
