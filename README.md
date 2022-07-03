# Image-Rotator

An application to rotate any image or set of images. This includes a GUI. The application can rotate by any angle, compress, change colour space and file type for any set of images of type .png or .jpg.

The application has been developed and tested on a windows computer only.

## Installation Guide

This application was developed using Python version 3.10.1. To install the related python packages run:

`python -m pip install -r requirements.txt`

### Running the Application

To run the application you must run the following command:

`python main.py`

This will open up the application GUI.

### Compiling the User Interface

If you have made a change to the user interface files (*.ui), you must convert them to python so that the changes are carried through when executed. This can be done using the compile python script:

`python main.py --compile --no-run`

It can also be done manually for the specific .ui file using:

`pyuic5 <user interface>.ui -o <python script>.py`

### Packaging the Application

To package the application run the following command:

`python main.py --compile --package --no-run`

This will package the application using PyInstaller. The packaged application (executable) will appear in the `dist/` folder.

In addition to this if the `--install` option is included, the executable will be copied to the user app data folder `Users/<User>/AppData/Local/ImageRotator`. The program will also create a desktop shortcut for the application as well as including it on the list of applications for a windows computer.

### Exection parameters

To get a list of the options when running `main.py` you can run:

`python main.py --help`

This will show there are the following options:
 - `--compile` - whether to compile the .ui files (default false, i.e. `--no-compile`)
 - `--package` - whether to package the application (default false, i.e. `--no-package`)
 - `--install` - whether to install the application on the computer (default false, i.e. `--no-install`)
 - `--run`- whether to run the application (default true, hence to not run use `--no-run`)

## User Guide

A user guide for how to use the application can be found by clicking on the "information" button in the top right corner of the main page interface. This opens a page with a full user guide for how to use the application.

## Developer Information

A developer information guide for the user interface components including all of the components names and types can be found in the `interface_documentation.md` file.

For the development of the application the following was used:
 - Qt designer v5.11.1
 - Python v3.10.1
 - PyQt5 v5.15.2
 - pyuic5 v5.15.7
 - PyInstaller v5.1

### Icons

All icons are from the Feature v4.29.0 icon library (https://feathericons.com).
