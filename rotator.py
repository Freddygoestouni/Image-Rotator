from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog

from PIL import Image
import os, sys


def start(filenames, destination, angle, direction, quality, colour, file_extension, progressBar=None):
    try:
        for filename in filenames:
            image = getImage(filename)

            image = rotate(image, angle, direction)

            image = colour_convert(image, colour)

            saveImage(destination, filename, image, quality, file_extension)

            #progressBar.setValue(int(filenames.index(filename)+1.0*100.0/len(filenames)))
        #progressBar.setValue(100)
        return True
    except:
        return False

def preview(filename, angle=None, direction=None, quality=None, colour=None):
    try:
        image = getImage(filename)

        if angle is not None and direction is not None:
            image = rotate(image, angle, direction)

        if colour is not None:
            image = colour_convert(image, colour)

        if image.mode == "RGB":
            r, g, b = image.split()
            image = Image.merge("RGB", (b, g, r))
        elif  image.mode == "RGBA":
            r, g, b, a = image.split()
            image = Image.merge("RGBA", (b, g, r, a))
        elif image.mode == "L":
            image = image.convert("RGBA")

        image = image.convert("RGBA")

        data = image.tobytes("raw", "RGBA")

        return data, image.size[0], image.size[1]
    except:
        return None

def getImage(filename):
    return Image.open(filename).convert('RGBA')

def rotate(image, angle, direction):
    if direction == "Clockwise":
        angle = 360-angle
    return image.rotate(angle, expand=True)

def colour_convert(image, colour):
    if colour == "Colour":
        return image.convert('RGB')
    elif colour == "Black/White":
        return image.convert('1')

def saveImage(destination, filename, image, quality, extension):
    filename = filename[filename.rindex("/"):]

    if extension != "Same as original":
        filename = filename[:filename.rindex(".")] + extension

    image.save(destination+filename, quality=quality, optimize=True)
