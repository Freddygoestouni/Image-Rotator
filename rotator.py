from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog

from PIL import Image
import os, sys


def start(filenames, angle, quality, destination, progressBar):
    try:
        for filename in filenames:
            image = getImage(filename)

            rotated = rotate(image, angle)

            saveImage(destination, filename, rotated, quality)

            progressBar.setValue(int(filenames.index(filename)+1.0*100.0/len(filenames)))
        progressBar.setValue(100)
        return True
    except:
        return False

def getImage(filename):
    return Image.open(filename).convert('RGBA')


def rotate(image, angle):
    return image.rotate(360-angle, expand=True)

def saveImage(destination, filename, image, quality):
    filename = filename[filename.rindex("/"):]
    image = image.convert('RGB')
    image.save(destination+filename, quality=quality, optimize=True)
